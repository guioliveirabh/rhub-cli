from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.rhubapiauthgroupupdate_group_response_200 import RhubapiauthgroupupdateGroupResponse200
from typing import cast
from typing import Dict
from ...models.rhubapiauthgroupupdate_group_json_body import RhubapiauthgroupupdateGroupJsonBody



def _get_kwargs(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupupdateGroupJsonBody,

) -> Dict[str, Any]:
    url = "{}/auth/group/{group_id}".format(
        client.base_url,group_id=group_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[RhubapiauthgroupupdateGroupResponse200]:
    if response.status_code == 200:
        response_200 = RhubapiauthgroupupdateGroupResponse200.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapiauthgroupupdateGroupResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupupdateGroupJsonBody,

) -> Response[RhubapiauthgroupupdateGroupResponse200]:
    kwargs = _get_kwargs(
        group_id=group_id,
client=client,
json_body=json_body,

    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupupdateGroupJsonBody,

) -> Optional[RhubapiauthgroupupdateGroupResponse200]:
    """ Update group in the database. Returns updated group data including extra
fields added by auth database.

See also [Keycloak API: GroupRepresentation](
  https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
 """

    return sync_detailed(
        group_id=group_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupupdateGroupJsonBody,

) -> Response[RhubapiauthgroupupdateGroupResponse200]:
    kwargs = _get_kwargs(
        group_id=group_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupupdateGroupJsonBody,

) -> Optional[RhubapiauthgroupupdateGroupResponse200]:
    """ Update group in the database. Returns updated group data including extra
fields added by auth database.

See also [Keycloak API: GroupRepresentation](
  https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
 """

    return (await asyncio_detailed(
        group_id=group_id,
client=client,
json_body=json_body,

    )).parsed
