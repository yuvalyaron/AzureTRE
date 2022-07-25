import math
import os
import logging
from distutils.util import strtobool
from datetime import datetime, timedelta

from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import generate_container_sas, ContainerSasPermissions, ContainerClient
from fastapi import HTTPException
from starlette import status

from api.routes.airlock_resource_helpers import RequestAccountDetails
from core import config
from azure.identity import DefaultAzureCredential
from models.domain.airlock_request import AirlockRequest, AirlockRequestStatus
from models.domain.authentication import User
from models.domain.workspace import Workspace

from resources import strings, constants


def get_storage_management_client():
    token_credential = DefaultAzureCredential(managed_identity_client_id=config.MANAGED_IDENTITY_CLIENT_ID,
                                              exclude_shared_token_cache_credential=True)
    return StorageManagementClient(credential=token_credential, subscription_id=config.SUBSCRIPTION_ID)


def get_account_and_rg_by_request(airlock_request: AirlockRequest, workspace: Workspace) -> RequestAccountDetails:
    tre_id = config.TRE_ID
    short_workspace_id = workspace.id[-4:]
    if airlock_request.requestType == constants.IMPORT_TYPE:
        if airlock_request.status == AirlockRequestStatus.Draft:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_IMPORT_EXTERNAL.format(tre_id),
                                         constants.CORE_RESOURCE_GROUP_NAME.format(tre_id))
        elif airlock_request.status == AirlockRequestStatus.Submitted:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_IMPORT_INPROGRESS.format(tre_id),
                                         constants.CORE_RESOURCE_GROUP_NAME.format(tre_id))
        elif airlock_request.status == AirlockRequestStatus.InReview:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_IMPORT_INPROGRESS.format(tre_id),
                                         constants.CORE_RESOURCE_GROUP_NAME.format(tre_id))
        elif airlock_request.status == AirlockRequestStatus.Approved:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_IMPORT_APPROVED.format(short_workspace_id),
                                         constants.WORKSPACE_RESOURCE_GROUP_NAME.format(tre_id, short_workspace_id))
        elif airlock_request.status == AirlockRequestStatus.Rejected:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_IMPORT_REJECTED.format(tre_id),
                                         constants.CORE_RESOURCE_GROUP_NAME.format(tre_id))
        elif airlock_request.status == AirlockRequestStatus.Blocked:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_IMPORT_BLOCKED.format(tre_id),
                                         constants.CORE_RESOURCE_GROUP_NAME.format(tre_id))
    else:
        if airlock_request.status == AirlockRequestStatus.Draft:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_EXPORT_INTERNAL.format(short_workspace_id),
                                         constants.WORKSPACE_RESOURCE_GROUP_NAME.format(tre_id, short_workspace_id))
        elif airlock_request.status in AirlockRequestStatus.Submitted:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_EXPORT_INPROGRESS.format(short_workspace_id),
                                         constants.WORKSPACE_RESOURCE_GROUP_NAME.format(tre_id, short_workspace_id))
        elif airlock_request.status == AirlockRequestStatus.InReview:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_EXPORT_INPROGRESS.format(short_workspace_id),
                                         constants.WORKSPACE_RESOURCE_GROUP_NAME.format(tre_id, short_workspace_id))
        elif airlock_request.status == AirlockRequestStatus.Approved:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_EXPORT_APPROVED.format(tre_id),
                                         constants.CORE_RESOURCE_GROUP_NAME.format(tre_id))
        elif airlock_request.status == AirlockRequestStatus.Rejected:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_EXPORT_REJECTED.format(short_workspace_id),
                                         constants.WORKSPACE_RESOURCE_GROUP_NAME.format(tre_id, short_workspace_id))
        elif airlock_request.status == AirlockRequestStatus.Blocked:
            return RequestAccountDetails(constants.STORAGE_ACCOUNT_NAME_EXPORT_BLOCKED.format(short_workspace_id),
                                         constants.WORKSPACE_RESOURCE_GROUP_NAME.format(tre_id, short_workspace_id))


def validate_user_allowed_to_access_storage_account(user: User, airlock_request: AirlockRequest):
    if "WorkspaceResearcher" not in user.roles and airlock_request.status != AirlockRequestStatus.InReview:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=strings.AIRLOCK_UNAUTHORIZED_TO_SA)

    if "WorkspaceOwner" not in user.roles and airlock_request.status == AirlockRequestStatus.InReview:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=strings.AIRLOCK_UNAUTHORIZED_TO_SA)
    return


def validate_request_status(airlock_request: AirlockRequest):
    if airlock_request.status in [AirlockRequestStatus.ApprovalInProgress,
                                  AirlockRequestStatus.RejectionInProgress,
                                  AirlockRequestStatus.BlockingInProgress]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=strings.AIRLOCK_REQUEST_IN_PROGRESS)
    elif airlock_request.status == AirlockRequestStatus.Cancelled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=strings.AIRLOCK_REQUEST_IS_CANCELED)
    else:
        return


def get_storage_account_key(storage_client: StorageManagementClient, request_account_details: RequestAccountDetails):
    return storage_client.storage_accounts.list_keys(request_account_details.account_rg,
                                                     request_account_details.account_name).keys[0].value


def get_required_permission(airlock_request: AirlockRequest) -> ContainerSasPermissions:
    if airlock_request.status == AirlockRequestStatus.Draft:
        return ContainerSasPermissions(read=True, write=True, list=True)
    else:
        return ContainerSasPermissions(read=True, list=True)


def get_airlock_request_container_sas_token(storage_client: StorageManagementClient,
                                            request_account_details: RequestAccountDetails,
                                            airlock_request: AirlockRequest):
    account_key = get_storage_account_key(storage_client, request_account_details)
    required_permission = get_required_permission(airlock_request)
    expiry = datetime.utcnow() + timedelta(hours=config.AIRLOCK_SAS_TOKEN_EXPIRY_PERIOD_IN_HOURS)

    # TODO: use user delegated key  https://github.com/microsoft/AzureTRE/issues/2185
    token = generate_container_sas(container_name=airlock_request.id,
                                   account_name=request_account_details.account_name,
                                   account_key=account_key,
                                   permission=required_permission,
                                   expiry=expiry)

    return "https://{}.blob.core.windows.net/{}?{}" \
        .format(request_account_details.account_name, airlock_request.id, token)


def validate_request_files_size_does_not_exceed_limit(airlock_request: AirlockRequest, workspace: Workspace, storage_client: StorageManagementClient):
    airlock_limit_in_mb = get_airlock_request_file_size_limit_in_mb(airlock_request)

    if airlock_limit_in_mb is math.inf:
        return

    container_size_in_mb = _get_container_size_in_mb(airlock_request, workspace, storage_client)
    if container_size_in_mb > airlock_limit_in_mb:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail=strings.AIRLOCK_REQUEST_FILE_SIZE_LIMIT_EXCEEDED.format(airlock_limit_in_mb))


def get_airlock_request_file_size_limit_in_mb(airlock_request: AirlockRequest):
    try:
        is_custom_limit_defined = "AIRLOCK_REQUEST_FILE_SIZE_LIMIT_IN_MB" in os.environ
        is_malware_scanning_enabled = bool(strtobool(os.environ["ENABLE_AIRLOCK_MALWARE_SCANNING"])) is True

        if not is_malware_scanning_enabled and not is_custom_limit_defined:
            return math.inf

        if airlock_request.requestType == constants.EXPORT_TYPE:
            return float(os.environ["AIRLOCK_REQUEST_FILE_SIZE_LIMIT_IN_MB"]) if is_custom_limit_defined else math.inf

        if is_malware_scanning_enabled and is_custom_limit_defined:
            return min(float(os.environ["MALWARE_SCANNING_FILE_SIZE_LIMIT_IN_MB"]), float(os.environ["AIRLOCK_REQUEST_FILE_SIZE_LIMIT_IN_MB"]))

        if is_malware_scanning_enabled:
            return float(os.environ["MALWARE_SCANNING_FILE_SIZE_LIMIT_IN_MB"])

        if is_custom_limit_defined:
            return float(os.environ["AIRLOCK_REQUEST_FILE_SIZE_LIMIT_IN_MB"])

        raise EnvironmentError('Invalid state - Airlock size limit could not be read.')

    except KeyError as e:
        error_message = f'Missing environment variable: {e}'
        logging.error(error_message)
        raise KeyError(error_message) from e


def _get_container_size_in_mb(airlock_request, workspace, storage_client):
    account_details = get_account_and_rg_by_request(airlock_request, workspace)
    container_url = get_airlock_request_container_sas_token(storage_client, account_details, airlock_request)
    container_client = ContainerClient.from_container_url(container_url)

    blob_list = container_client.list_blobs()
    total_size_in_bytes = 0
    for blob in blob_list:
        total_size_in_bytes += blob.size

    total_size_in_mb = total_size_in_bytes / 1024 / 1024
    return total_size_in_mb
