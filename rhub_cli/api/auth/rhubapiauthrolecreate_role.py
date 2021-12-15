from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthrolecreate_role_json_body import RhubapiauthrolecreateRoleJsonBody
from ...models.rhubapiauthrolecreate_role_response_200 import RhubapiauthrolecreateRoleResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthrolecreateRoleJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/role".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[RhubapiauthrolecreateRoleResponse200]:
    if response.status_code == 200:
        response_200 = RhubapiauthrolecreateRoleResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapiauthrolecreateRoleResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthrolecreateRoleJsonBody,
) -> Response[RhubapiauthrolecreateRoleResponse200]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthrolecreateRoleJsonBody,
) -> Optional[RhubapiauthrolecreateRoleResponse200]:
    """Create a role in the database. Returns created role data with extra
    fields added by auth database (UUID and other fields).

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthrolecreateRoleJsonBody,
) -> Response[RhubapiauthrolecreateRoleResponse200]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthrolecreateRoleJsonBody,
) -> Optional[RhubapiauthrolecreateRoleResponse200]:
    """Create a role in the database. Returns created role data with extra
    fields added by auth database (UUID and other fields).

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
