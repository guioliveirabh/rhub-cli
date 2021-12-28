from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabregionadd_region_product_json_body import RhubapilabregionaddRegionProductJsonBody
from ...models.rhubapilabregionadd_region_product_response_default import (
    RhubapilabregionaddRegionProductResponseDefault,
)
from ...types import Response


def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregionaddRegionProductJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}/products".format(client.base_url, region_id=region_id)

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
) -> Optional[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]:
    if response.status_code == 204:
        response_204 = None

        return response_204

    else:
        response_default = RhubapilabregionaddRegionProductResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]:
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
    json_body: RhubapilabregionaddRegionProductJsonBody,
) -> Response[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]:
    """Add product to region or disable/enable product in region

    Args:
        region_id (int):
        json_body (RhubapilabregionaddRegionProductJsonBody):

    Returns:
        Response[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregionaddRegionProductJsonBody,
) -> Optional[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]:
    """Add product to region or disable/enable product in region

    Args:
        region_id (int):
        json_body (RhubapilabregionaddRegionProductJsonBody):

    Returns:
        Response[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregionaddRegionProductJsonBody,
) -> Response[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]:
    """Add product to region or disable/enable product in region

    Args:
        region_id (int):
        json_body (RhubapilabregionaddRegionProductJsonBody):

    Returns:
        Response[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregionaddRegionProductJsonBody,
) -> Optional[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]:
    """Add product to region or disable/enable product in region

    Args:
        region_id (int):
        json_body (RhubapilabregionaddRegionProductJsonBody):

    Returns:
        Response[Union[Any, RhubapilabregionaddRegionProductResponseDefault]]
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
