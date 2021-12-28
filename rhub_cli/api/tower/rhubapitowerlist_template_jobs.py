from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapitowerlist_template_jobs_filter import RhubapitowerlistTemplateJobsFilter
from ...models.rhubapitowerlist_template_jobs_response_200 import RhubapitowerlistTemplateJobsResponse200
from ...models.rhubapitowerlist_template_jobs_response_default import RhubapitowerlistTemplateJobsResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    template_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapitowerlistTemplateJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/tower/template/{template_id}/jobs".format(client.base_url, template_id=template_id)

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
) -> Optional[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapitowerlistTemplateJobsResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapitowerlistTemplateJobsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    template_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapitowerlistTemplateJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]:
    """List Tower template jobs

    Args:
        template_id (int):
        filter_ (Union[Unset, None, RhubapitowerlistTemplateJobsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
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
    template_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapitowerlistTemplateJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]:
    """List Tower template jobs

    Args:
        template_id (int):
        filter_ (Union[Unset, None, RhubapitowerlistTemplateJobsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    template_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapitowerlistTemplateJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]:
    """List Tower template jobs

    Args:
        template_id (int):
        filter_ (Union[Unset, None, RhubapitowerlistTemplateJobsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    template_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapitowerlistTemplateJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]:
    """List Tower template jobs

    Args:
        template_id (int):
        filter_ (Union[Unset, None, RhubapitowerlistTemplateJobsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubapitowerlistTemplateJobsResponse200, RhubapitowerlistTemplateJobsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
            filter_=filter_,
            page=page,
            limit=limit,
        )
    ).parsed
