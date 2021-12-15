from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import cast, List
from typing import Optional
from ...types import UNSET, Unset
from typing import Dict
from ...models.rhubapilabproductlist_product_regions_response_200_item import RhubapilabproductlistProductRegionsResponse200Item
from ...models.rhubapilabproductlist_product_regions_filter import RhubapilabproductlistProductRegionsFilter
from typing import cast
from typing import Union



def _get_kwargs(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabproductlistProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Dict[str, Any]:
    url = "{}/lab/product/{product_id}/regions".format(
        client.base_url,product_id=product_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    json_filter_: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.to_dict() if filter_ else None

    params: Dict[str, Any] = {
        "page": page,
        "limit": limit,
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


def _parse_response(*, response: httpx.Response) -> Optional[List[RhubapilabproductlistProductRegionsResponse200Item]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = RhubapilabproductlistProductRegionsResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[RhubapilabproductlistProductRegionsResponse200Item]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabproductlistProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Response[List[RhubapilabproductlistProductRegionsResponse200Item]]:
    kwargs = _get_kwargs(
        product_id=product_id,
client=client,
filter_=filter_,
page=page,
limit=limit,

    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabproductlistProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Optional[List[RhubapilabproductlistProductRegionsResponse200Item]]:
    """  """

    return sync_detailed(
        product_id=product_id,
client=client,
filter_=filter_,
page=page,
limit=limit,

    ).parsed

async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabproductlistProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Response[List[RhubapilabproductlistProductRegionsResponse200Item]]:
    kwargs = _get_kwargs(
        product_id=product_id,
client=client,
filter_=filter_,
page=page,
limit=limit,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabproductlistProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Optional[List[RhubapilabproductlistProductRegionsResponse200Item]]:
    """  """

    return (await asyncio_detailed(
        product_id=product_id,
client=client,
filter_=filter_,
page=page,
limit=limit,

    )).parsed
