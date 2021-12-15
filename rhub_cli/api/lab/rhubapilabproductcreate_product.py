from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabproductcreate_product_json_body import RhubapilabproductcreateProductJsonBody
from ...models.rhubapilabproductcreate_product_response_default import RhubapilabproductcreateProductResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabproductcreateProductJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/product".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapilabproductcreateProductResponseDefault]]:
    if response.status_code == 200:
        response_200 = None

        return response_200

    else:
        response_default = RhubapilabproductcreateProductResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapilabproductcreateProductResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabproductcreateProductJsonBody,
) -> Response[Union[Any, RhubapilabproductcreateProductResponseDefault]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabproductcreateProductJsonBody,
) -> Optional[Union[Any, RhubapilabproductcreateProductResponseDefault]]:
    """`tower_template_name_create` is the Tower template name to create the
    cluster, and `tower_template_name_delete` to delete.
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabproductcreateProductJsonBody,
) -> Response[Union[Any, RhubapilabproductcreateProductResponseDefault]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabproductcreateProductJsonBody,
) -> Optional[Union[Any, RhubapilabproductcreateProductResponseDefault]]:
    """`tower_template_name_create` is the Tower template name to create the
    cluster, and `tower_template_name_delete` to delete.
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
