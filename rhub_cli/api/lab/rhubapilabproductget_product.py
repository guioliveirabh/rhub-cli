from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.rhubapilabproductget_product_response_200 import RhubapilabproductgetProductResponse200
from typing import cast
from typing import Dict



def _get_kwargs(
    product_id: int,
    *,
    client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/lab/product/{product_id}".format(
        client.base_url,product_id=product_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapilabproductgetProductResponse200]]:
    if response.status_code == 200:
        response_200 = RhubapilabproductgetProductResponse200.from_dict(response.json())



        return response_200
    if response.status_code == 404:
        response_404 = None

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapilabproductgetProductResponse200]]:
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

) -> Response[Union[Any, RhubapilabproductgetProductResponse200]]:
    kwargs = _get_kwargs(
        product_id=product_id,
client=client,

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

) -> Optional[Union[Any, RhubapilabproductgetProductResponse200]]:
    """  """

    return sync_detailed(
        product_id=product_id,
client=client,

    ).parsed

async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, RhubapilabproductgetProductResponse200]]:
    kwargs = _get_kwargs(
        product_id=product_id,
client=client,

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

) -> Optional[Union[Any, RhubapilabproductgetProductResponse200]]:
    """  """

    return (await asyncio_detailed(
        product_id=product_id,
client=client,

    )).parsed
