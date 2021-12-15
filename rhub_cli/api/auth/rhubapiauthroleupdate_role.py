from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import cast
from ...models.rhubapiauthroleupdate_role_json_body import RhubapiauthroleupdateRoleJsonBody
from typing import Dict
from ...models.rhubapiauthroleupdate_role_response_200 import RhubapiauthroleupdateRoleResponse200



def _get_kwargs(
    role_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthroleupdateRoleJsonBody,

) -> Dict[str, Any]:
    url = "{}/auth/role/{role_id}".format(
        client.base_url,role_id=role_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[RhubapiauthroleupdateRoleResponse200]:
    if response.status_code == 200:
        response_200 = RhubapiauthroleupdateRoleResponse200.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapiauthroleupdateRoleResponse200]:
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
    json_body: RhubapiauthroleupdateRoleJsonBody,

) -> Response[RhubapiauthroleupdateRoleResponse200]:
    kwargs = _get_kwargs(
        role_id=role_id,
client=client,
json_body=json_body,

    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    role_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthroleupdateRoleJsonBody,

) -> Optional[RhubapiauthroleupdateRoleResponse200]:
    """ Update role in the database. Returns updated role data including extra
fields added by auth database.

See [Keycloak API: RoleRepresentation](
  https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
 """

    return sync_detailed(
        role_id=role_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthroleupdateRoleJsonBody,

) -> Response[RhubapiauthroleupdateRoleResponse200]:
    kwargs = _get_kwargs(
        role_id=role_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    role_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthroleupdateRoleJsonBody,

) -> Optional[RhubapiauthroleupdateRoleResponse200]:
    """ Update role in the database. Returns updated role data including extra
fields added by auth database.

See [Keycloak API: RoleRepresentation](
  https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
 """

    return (await asyncio_detailed(
        role_id=role_id,
client=client,
json_body=json_body,

    )).parsed
