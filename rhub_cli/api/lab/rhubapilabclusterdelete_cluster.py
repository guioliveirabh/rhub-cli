from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabclusterdelete_cluster_response_default import RhubapilabclusterdeleteClusterResponseDefault
from ...types import Response


def _get_kwargs(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/cluster/{cluster_id}".format(client.base_url, cluster_id=cluster_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]:
    if response.status_code == 204:
        response_204 = None

        return response_204

    else:
        response_default = RhubapilabclusterdeleteClusterResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]:
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
) -> Response[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]:
    """Delete cluster

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]:
    """Delete cluster

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]:
    """Delete cluster

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]:
    """Delete cluster

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubapilabclusterdeleteClusterResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
        )
    ).parsed
