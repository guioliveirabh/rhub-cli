from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import cast, List
from typing import Optional
from ...models.rhubapilabregionlist_region_products_filter import RhubapilabregionlistRegionProductsFilter
from ...types import UNSET, Unset
from typing import Dict
from ...models.rhubapilabregionlist_region_products_response_200_item import RhubapilabregionlistRegionProductsResponse200Item
from typing import cast
from typing import Union



def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionProductsFilter] = UNSET,

) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}/products".format(
        client.base_url,region_id=region_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    json_filter_: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.to_dict() if filter_ else None

    params: Dict[str, Any] = {
    }
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


def _parse_response(*, response: httpx.Response) -> Optional[List[RhubapilabregionlistRegionProductsResponse200Item]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = RhubapilabregionlistRegionProductsResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[RhubapilabregionlistRegionProductsResponse200Item]]:
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

) -> Response[List[RhubapilabregionlistRegionProductsResponse200Item]]:
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

) -> Optional[List[RhubapilabregionlistRegionProductsResponse200Item]]:
    """  """

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

) -> Response[List[RhubapilabregionlistRegionProductsResponse200Item]]:
    kwargs = _get_kwargs(
        region_id=region_id,
client=client,
filter_=filter_,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionProductsFilter] = UNSET,

) -> Optional[List[RhubapilabregionlistRegionProductsResponse200Item]]:
    """  """

    return (await asyncio_detailed(
        region_id=region_id,
client=client,
filter_=filter_,

    )).parsed
