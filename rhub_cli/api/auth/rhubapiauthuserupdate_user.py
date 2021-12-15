from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import cast
from ...models.rhubapiauthuserupdate_user_response_200 import RhubapiauthuserupdateUserResponse200
from ...models.rhubapiauthuserupdate_user_json_body import RhubapiauthuserupdateUserJsonBody
from typing import Dict



def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserupdateUserJsonBody,

) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}".format(
        client.base_url,user_id=user_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[RhubapiauthuserupdateUserResponse200]:
    if response.status_code == 200:
        response_200 = RhubapiauthuserupdateUserResponse200.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapiauthuserupdateUserResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserupdateUserJsonBody,

) -> Response[RhubapiauthuserupdateUserResponse200]:
    kwargs = _get_kwargs(
        user_id=user_id,
client=client,
json_body=json_body,

    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserupdateUserJsonBody,

) -> Optional[RhubapiauthuserupdateUserResponse200]:
    """ Update user in the database. Returns updated user data including extra
fields added by auth database.

See also [Keycloak API: UserRepresentation](
  https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
 """

    return sync_detailed(
        user_id=user_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserupdateUserJsonBody,

) -> Response[RhubapiauthuserupdateUserResponse200]:
    kwargs = _get_kwargs(
        user_id=user_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserupdateUserJsonBody,

) -> Optional[RhubapiauthuserupdateUserResponse200]:
    """ Update user in the database. Returns updated user data including extra
fields added by auth database.

See also [Keycloak API: UserRepresentation](
  https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
 """

    return (await asyncio_detailed(
        user_id=user_id,
client=client,
json_body=json_body,

    )).parsed
