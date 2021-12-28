from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabregionlist_region_products_filter import RhubapilabregionlistRegionProductsFilter
from ...models.rhubapilabregionlist_region_products_response_200_item import (
    RhubapilabregionlistRegionProductsResponse200Item,
)
from ...models.rhubapilabregionlist_region_products_response_default import (
    RhubapilabregionlistRegionProductsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionProductsFilter] = UNSET,
) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}/products".format(client.base_url, region_id=region_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_filter_: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.to_dict() if filter_ else None

    params: Dict[str, Any] = {}
    if not isinstance(json_filter_, Unset) and json_filter_ is not None:
        params.update(json_filter_)
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubapilabregionlistRegionProductsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubapilabregionlistRegionProductsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]
]:
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
    filter_: Union[Unset, None, RhubapilabregionlistRegionProductsFilter] = UNSET,
) -> Response[
    Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]
]:
    """Get list of products that can be installed in the selected region.

    Args:
        region_id (int):
        filter_ (Union[Unset, None, RhubapilabregionlistRegionProductsFilter]):

    Returns:
        Response[Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        filter_=filter_,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    region_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionProductsFilter] = UNSET,
) -> Optional[
    Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]
]:
    """Get list of products that can be installed in the selected region.

    Args:
        region_id (int):
        filter_ (Union[Unset, None, RhubapilabregionlistRegionProductsFilter]):

    Returns:
        Response[Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]]
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionProductsFilter] = UNSET,
) -> Response[
    Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]
]:
    """Get list of products that can be installed in the selected region.

    Args:
        region_id (int):
        filter_ (Union[Unset, None, RhubapilabregionlistRegionProductsFilter]):

    Returns:
        Response[Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        filter_=filter_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionProductsFilter] = UNSET,
) -> Optional[
    Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]
]:
    """Get list of products that can be installed in the selected region.

    Args:
        region_id (int):
        filter_ (Union[Unset, None, RhubapilabregionlistRegionProductsFilter]):

    Returns:
        Response[Union[List[RhubapilabregionlistRegionProductsResponse200Item], RhubapilabregionlistRegionProductsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
            filter_=filter_,
        )
    ).parsed
