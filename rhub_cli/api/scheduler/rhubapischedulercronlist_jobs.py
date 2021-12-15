from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import Optional
from ...models.rhubapischedulercronlist_jobs_response_200 import RhubapischedulercronlistJobsResponse200
from ...types import UNSET, Unset
from typing import Dict
from ...models.rhubapischedulercronlist_jobs_filter import RhubapischedulercronlistJobsFilter
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapischedulercronlistJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Dict[str, Any]:
    url = "{}/scheduler/cron".format(
        client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[RhubapischedulercronlistJobsResponse200]:
    if response.status_code == 200:
        response_200 = RhubapischedulercronlistJobsResponse200.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapischedulercronlistJobsResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapischedulercronlistJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Response[RhubapischedulercronlistJobsResponse200]:
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
    filter_: Union[Unset, None, RhubapischedulercronlistJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Optional[RhubapischedulercronlistJobsResponse200]:
    """  """

    return sync_detailed(
        client=client,
filter_=filter_,
page=page,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapischedulercronlistJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Response[RhubapischedulercronlistJobsResponse200]:
    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubapischedulercronlistJobsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,

) -> Optional[RhubapischedulercronlistJobsResponse200]:
    """  """

    return (await asyncio_detailed(
        client=client,
filter_=filter_,
page=page,
limit=limit,

    )).parsed
