from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.rhubapiauthuserdelete_user_group_json_body import RhubapiauthuserdeleteUserGroupJsonBody
from typing import Dict
from typing import cast



def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserdeleteUserGroupJsonBody,

) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}/groups".format(
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




def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserdeleteUserGroupJsonBody,

) -> Response[Any]:
    kwargs = _get_kwargs(
        user_id=user_id,
client=client,
json_body=json_body,

    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserdeleteUserGroupJsonBody,

) -> Response[Any]:
    kwargs = _get_kwargs(
        user_id=user_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(
            **kwargs
        )

    return _build_response(response=response)

