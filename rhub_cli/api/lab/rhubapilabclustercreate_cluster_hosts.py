from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabclustercreate_cluster_hosts_json_body_item import (
    RhubapilabclustercreateClusterHostsJsonBodyItem,
)
from ...models.rhubapilabclustercreate_cluster_hosts_response_200_item import (
    RhubapilabclustercreateClusterHostsResponse200Item,
)
from ...models.rhubapilabclustercreate_cluster_hosts_response_default import (
    RhubapilabclustercreateClusterHostsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: List[RhubapilabclustercreateClusterHostsJsonBodyItem],
) -> Dict[str, Any]:
    url = "{}/lab/cluster/{cluster_id}/hosts".format(client.base_url, cluster_id=cluster_id)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.text
        for response_200_item_data in _response_200:
            response_200_item = RhubapilabclustercreateClusterHostsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubapilabclustercreateClusterHostsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: List[RhubapilabclustercreateClusterHostsJsonBodyItem],
) -> Response[
    Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]
]:
    """Create or update cluster hosts

    Args:
        cluster_id (int):
        json_body (List[RhubapilabclustercreateClusterHostsJsonBodyItem]):

    Returns:
        Response[Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]]
    """

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


def sync(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: List[RhubapilabclustercreateClusterHostsJsonBodyItem],
) -> Optional[
    Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]
]:
    """Create or update cluster hosts

    Args:
        cluster_id (int):
        json_body (List[RhubapilabclustercreateClusterHostsJsonBodyItem]):

    Returns:
        Response[Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: List[RhubapilabclustercreateClusterHostsJsonBodyItem],
) -> Response[
    Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]
]:
    """Create or update cluster hosts

    Args:
        cluster_id (int):
        json_body (List[RhubapilabclustercreateClusterHostsJsonBodyItem]):

    Returns:
        Response[Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: List[RhubapilabclustercreateClusterHostsJsonBodyItem],
) -> Optional[
    Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]
]:
    """Create or update cluster hosts

    Args:
        cluster_id (int):
        json_body (List[RhubapilabclustercreateClusterHostsJsonBodyItem]):

    Returns:
        Response[Union[List[RhubapilabclustercreateClusterHostsResponse200Item], RhubapilabclustercreateClusterHostsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
