from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import cast
from typing import cast, List
from typing import Dict
from ...models.rhubapilabclustercreate_cluster_hosts_json_body_item import RhubapilabclustercreateClusterHostsJsonBodyItem



def _get_kwargs(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: List[RhubapilabclustercreateClusterHostsJsonBodyItem],

) -> Dict[str, Any]:
    url = "{}/lab/cluster/{cluster_id}/hosts".format(
        client.base_url,cluster_id=cluster_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)






    

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
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: List[RhubapilabclustercreateClusterHostsJsonBodyItem],

) -> Response[Any]:
    kwargs = _get_kwargs(
        cluster_id=cluster_id,
client=client,
json_body=json_body,

    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: List[RhubapilabclustercreateClusterHostsJsonBodyItem],

) -> Response[Any]:
    kwargs = _get_kwargs(
        cluster_id=cluster_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(
            **kwargs
        )

    return _build_response(response=response)

