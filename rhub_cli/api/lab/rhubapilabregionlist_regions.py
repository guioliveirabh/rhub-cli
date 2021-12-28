from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabregionlist_regions_filter import RhubapilabregionlistRegionsFilter
from ...models.rhubapilabregionlist_regions_response_200 import RhubapilabregionlistRegionsResponse200
from ...models.rhubapilabregionlist_regions_response_default import RhubapilabregionlistRegionsResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/lab/region".format(client.base_url)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapilabregionlistRegionsResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapilabregionlistRegionsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]:
    """Get region list

    Args:
        filter_ (Union[Unset, None, RhubapilabregionlistRegionsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]:
    """Get region list

    Args:
        filter_ (Union[Unset, None, RhubapilabregionlistRegionsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]:
    """Get region list

    Args:
        filter_ (Union[Unset, None, RhubapilabregionlistRegionsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapilabregionlistRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]:
    """Get region list

    Args:
        filter_ (Union[Unset, None, RhubapilabregionlistRegionsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubapilabregionlistRegionsResponse200, RhubapilabregionlistRegionsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            page=page,
            limit=limit,
        )
    ).parsed
