import math
from fastapi import HTTPException, status
import pytest
from services.airlock import validate_user_allowed_to_access_storage_account, get_required_permission, get_airlock_request_file_size_limit_in_mb
from models.domain.airlock_resource import AirlockResourceType
from models.domain.airlock_request import AirlockRequest, AirlockRequestStatus, AirlockRequestType
from tests_ma.test_api.conftest import create_workspace_owner_user, create_workspace_researcher_user

MALWARE_SCANNING_FILE_SIZE_LIMIT_IN_MB = 2048


def sample_airlock_request(status=AirlockRequestStatus.Draft, request_type=AirlockRequestType.Import):
    airlock_request = AirlockRequest(
        id="AIRLOCK_REQUEST_ID",
        resourceType=AirlockResourceType.AirlockRequest,
        workspaceId="WORKSPACE_ID",
        requestType=request_type,
        files=[],
        businessJustification="some test reason",
        status=status
    )
    return airlock_request


def test_validate_user_is_allowed_to_access_sa_blocks_access_as_expected():
    # Workspace owner can access only in review
    ws_owner_user = create_workspace_owner_user()
    draft_airlock_request = sample_airlock_request()
    with pytest.raises(HTTPException) as ex:
        validate_user_allowed_to_access_storage_account(
            user=ws_owner_user,
            airlock_request=draft_airlock_request
        )

    assert ex.value.status_code == status.HTTP_403_FORBIDDEN

    researcher_user = create_workspace_researcher_user()
    review_airlock_request = sample_airlock_request(AirlockRequestStatus.InReview)
    with pytest.raises(HTTPException) as ex:
        validate_user_allowed_to_access_storage_account(
            user=researcher_user,
            airlock_request=review_airlock_request
        )

    assert ex.value.status_code == status.HTTP_403_FORBIDDEN


def test_validate_user_is_allowed_to_access_grants_access_to_user_with_a_valid_role():
    # Workspace owner can access only in review
    ws_owner_user = create_workspace_owner_user()
    draft_airlock_request = sample_airlock_request(AirlockRequestStatus.InReview)

    assert (validate_user_allowed_to_access_storage_account(
        user=ws_owner_user,
        airlock_request=draft_airlock_request) is None)

    researcher_user = create_workspace_researcher_user()
    review_airlock_request = sample_airlock_request(AirlockRequestStatus.Approved)
    assert (
        validate_user_allowed_to_access_storage_account(
            user=researcher_user,
            airlock_request=review_airlock_request
        ) is None)


@pytest.mark.parametrize('airlock_status',
                         [AirlockRequestStatus.Submitted,
                          AirlockRequestStatus.InReview,
                          AirlockRequestStatus.ApprovalInProgress,
                          AirlockRequestStatus.Approved,
                          AirlockRequestStatus.RejectionInProgress,
                          AirlockRequestStatus.Rejected,
                          AirlockRequestStatus.Cancelled,
                          AirlockRequestStatus.BlockingInProgress,
                          AirlockRequestStatus.Blocked])
def test_get_required_permission_return_read_only_permissions_for_non_draft_requests(airlock_status):
    airlock_request = sample_airlock_request(airlock_status)
    permissions = get_required_permission(airlock_request)
    assert permissions.write is False
    assert permissions.read is True


@pytest.mark.parametrize("is_malware_scanning_enabled, custom_limit, request_type, expected_limit", [
                         (True, 5.17, AirlockRequestType.Export, 5.17),
                         (True, 5.17, AirlockRequestType.Import, 5.17),
                         (True, None, AirlockRequestType.Export, math.inf),
                         (True, None, AirlockRequestType.Import, MALWARE_SCANNING_FILE_SIZE_LIMIT_IN_MB),
                         (False, 5.17, AirlockRequestType.Export, 5.17),
                         (False, 5.17, AirlockRequestType.Import, 5.17),
                         (False, None, AirlockRequestType.Export, math.inf),
                         (False, None, AirlockRequestType.Import, math.inf),
                         (True, MALWARE_SCANNING_FILE_SIZE_LIMIT_IN_MB + 1, AirlockRequestType.Import, MALWARE_SCANNING_FILE_SIZE_LIMIT_IN_MB),
                         ])
def test_get_airlock_request_file_size_limit_in_mb_returns_correct_value(is_malware_scanning_enabled, custom_limit, request_type, expected_limit, monkeypatch):
    if custom_limit:
        monkeypatch.setenv('AIRLOCK_REQUEST_FILE_SIZE_LIMIT_IN_MB', custom_limit)

    monkeypatch.setenv('ENABLE_AIRLOCK_MALWARE_SCANNING', is_malware_scanning_enabled)
    monkeypatch.setenv('MALWARE_SCANNING_FILE_SIZE_LIMIT_IN_MB', MALWARE_SCANNING_FILE_SIZE_LIMIT_IN_MB)

    review_airlock_request = sample_airlock_request(request_type=request_type)
    limit = get_airlock_request_file_size_limit_in_mb(review_airlock_request)
    assert limit == expected_limit
