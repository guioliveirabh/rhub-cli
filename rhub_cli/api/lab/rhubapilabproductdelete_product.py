from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabproductdelete_product_response_default import RhubapilabproductdeleteProductResponseDefault
from ...types import Response


def _get_kwargs(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/product/{product_id}".format(client.base_url, product_id=product_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapilabproductdeleteProductResponseDefault]]:
    if response.status_code == 204:
        response_204 = None

        return response_204

    else:
        response_default = RhubapilabproductdeleteProductResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapilabproductdeleteProductResponseDefault]]:
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
) -> Response[Union[Any, RhubapilabproductdeleteProductResponseDefault]]:
    """Delete product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubapilabproductdeleteProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapilabproductdeleteProductResponseDefault]]:
    """Delete product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubapilabproductdeleteProductResponseDefault]]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapilabproductdeleteProductResponseDefault]]:
    """Delete product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubapilabproductdeleteProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapilabproductdeleteProductResponseDefault]]:
    """Delete product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubapilabproductdeleteProductResponseDefault]]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
        )
    ).parsed
