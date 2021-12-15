from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthroleget_role_response_200 import RhubapiauthrolegetRoleResponse200
from ...types import Response


def _get_kwargs(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/role/{role_id}".format(client.base_url, role_id=role_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RhubapiauthrolegetRoleResponse200]:
    if response.status_code == 200:
        response_200 = RhubapiauthrolegetRoleResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapiauthrolegetRoleResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[RhubapiauthrolegetRoleResponse200]:
    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[RhubapiauthrolegetRoleResponse200]:
    """Returns role data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `description` and others.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[RhubapiauthrolegetRoleResponse200]:
    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[RhubapiauthrolegetRoleResponse200]:
    """Returns role data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `description` and others.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
        )
    ).parsed
