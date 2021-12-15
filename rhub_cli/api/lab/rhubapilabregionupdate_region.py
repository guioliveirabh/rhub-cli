from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabregionupdate_region_json_body import RhubapilabregionupdateRegionJsonBody
from ...models.rhubapilabregionupdate_region_response_default import RhubapilabregionupdateRegionResponseDefault
from ...types import Response


def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregionupdateRegionJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}".format(client.base_url, region_id=region_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapilabregionupdateRegionResponseDefault]]:
    if response.status_code == 200:
        response_200 = None

        return response_200

    else:
        response_default = RhubapilabregionupdateRegionResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapilabregionupdateRegionResponseDefault]]:
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
    json_body: RhubapilabregionupdateRegionJsonBody,
) -> Response[Union[Any, RhubapilabregionupdateRegionResponseDefault]]:
    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregionupdateRegionJsonBody,
) -> Optional[Union[Any, RhubapilabregionupdateRegionResponseDefault]]:
    """ """

    return sync_detailed(
        region_id=region_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregionupdateRegionJsonBody,
) -> Response[Union[Any, RhubapilabregionupdateRegionResponseDefault]]:
    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregionupdateRegionJsonBody,
) -> Optional[Union[Any, RhubapilabregionupdateRegionResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
