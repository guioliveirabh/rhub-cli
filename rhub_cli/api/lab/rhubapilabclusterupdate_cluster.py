from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabclusterupdate_cluster_json_body import RhubapilabclusterupdateClusterJsonBody
from ...models.rhubapilabclusterupdate_cluster_response_200 import RhubapilabclusterupdateClusterResponse200
from ...models.rhubapilabclusterupdate_cluster_response_default import RhubapilabclusterupdateClusterResponseDefault
from ...types import Response


def _get_kwargs(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabclusterupdateClusterJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/cluster/{cluster_id}".format(client.base_url, cluster_id=cluster_id)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapilabclusterupdateClusterResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapilabclusterupdateClusterResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]:
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
    json_body: RhubapilabclusterupdateClusterJsonBody,
) -> Response[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]:
    """Update cluster

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster) for more info.

    Args:
        cluster_id (int):
        json_body (RhubapilabclusterupdateClusterJsonBody):

    Returns:
        Response[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabclusterupdateClusterJsonBody,
) -> Optional[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]:
    """Update cluster

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster) for more info.

    Args:
        cluster_id (int):
        json_body (RhubapilabclusterupdateClusterJsonBody):

    Returns:
        Response[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]
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
    json_body: RhubapilabclusterupdateClusterJsonBody,
) -> Response[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]:
    """Update cluster

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster) for more info.

    Args:
        cluster_id (int):
        json_body (RhubapilabclusterupdateClusterJsonBody):

    Returns:
        Response[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabclusterupdateClusterJsonBody,
) -> Optional[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]:
    """Update cluster

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster) for more info.

    Args:
        cluster_id (int):
        json_body (RhubapilabclusterupdateClusterJsonBody):

    Returns:
        Response[Union[RhubapilabclusterupdateClusterResponse200, RhubapilabclusterupdateClusterResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
