from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabregionget_region_response_200 import RhubapilabregiongetRegionResponse200
from ...models.rhubapilabregionget_region_response_default import RhubapilabregiongetRegionResponseDefault
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, RhubapilabregiongetRegionResponse200, RhubapilabregiongetRegionResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapilabregiongetRegionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = None

        return response_404

    else:
        response_default = RhubapilabregiongetRegionResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubapilabregiongetRegionResponse200, RhubapilabregiongetRegionResponseDefault]]:
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
) -> Response[Union[Any, RhubapilabregiongetRegionResponse200, RhubapilabregiongetRegionResponseDefault]]:
    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
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
) -> Optional[Union[Any, RhubapilabregiongetRegionResponse200, RhubapilabregiongetRegionResponseDefault]]:
    """ """

    return sync_detailed(
        region_id=region_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapilabregiongetRegionResponse200, RhubapilabregiongetRegionResponseDefault]]:
    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapilabregiongetRegionResponse200, RhubapilabregiongetRegionResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
        )
    ).parsed
