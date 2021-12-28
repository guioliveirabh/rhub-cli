from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabregiondelete_region_response_default import RhubapilabregiondeleteRegionResponseDefault
from ...types import Response


def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}".format(client.base_url, region_id=region_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]:
    if response.status_code == 204:
        response_204 = None

        return response_204

    else:
        response_default = RhubapilabregiondeleteRegionResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]:
    """Delete region

    Args:
        region_id (int):

    Returns:
        Response[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]:
    """Delete region

    Args:
        region_id (int):

    Returns:
        Response[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]:
    """Delete region

    Args:
        region_id (int):

    Returns:
        Response[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]:
    """Delete region

    Args:
        region_id (int):

    Returns:
        Response[Union[Any, RhubapilabregiondeleteRegionResponseDefault]]
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
        )
    ).parsed
