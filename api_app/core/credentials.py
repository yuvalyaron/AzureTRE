from contextlib import asynccontextmanager
from core import config
from azure.core.credentials import TokenCredential
from urllib.parse import urlparse

from azure.identity import (
    DefaultAzureCredential,
    ManagedIdentityCredential,
    ChainedTokenCredential,
)
from azure.identity.aio import (
    DefaultAzureCredential as DefaultAzureCredentialASync,
    ManagedIdentityCredential as ManagedIdentityCredentialASync,
    ChainedTokenCredential as ChainedTokenCredentialASync,
)


def get_credential() -> TokenCredential:
    managed_identity = config.MANAGED_IDENTITY_CLIENT_ID
    if managed_identity:
        return ChainedTokenCredential(
            ManagedIdentityCredential(client_id=managed_identity)
        )
    else:
        return DefaultAzureCredential(authority=urlparse(config.AAD_AUTHORITY_URL).netloc)


@asynccontextmanager
async def get_credential_async() -> TokenCredential:
    """
    Context manager which yields the default credentials.
    """
    managed_identity = config.MANAGED_IDENTITY_CLIENT_ID
    credential = (
        ChainedTokenCredentialASync(
            ManagedIdentityCredentialASync(client_id=managed_identity)
        )
        if managed_identity
        else DefaultAzureCredentialASync(authority=urlparse(config.AAD_AUTHORITY_URL).netloc)
    )
    yield credential
    await credential.close()
