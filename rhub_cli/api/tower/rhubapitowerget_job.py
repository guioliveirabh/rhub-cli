from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import cast
from ...models.rhubapitowerget_job_response_200 import RhubapitowergetJobResponse200
from typing import Dict



def _get_kwargs(
    job_id: int,
    *,
    client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/tower/job/{job_id}".format(
        client.base_url,job_id=job_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RhubapitowergetJobResponse200]:
    if response.status_code == 200:
        response_200 = RhubapitowergetJobResponse200.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapitowergetJobResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    job_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[RhubapitowergetJobResponse200]:
    kwargs = _get_kwargs(
        job_id=job_id,
client=client,

    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    job_id: int,
    *,
    client: AuthenticatedClient,

) -> Optional[RhubapitowergetJobResponse200]:
    """  """

    return sync_detailed(
        job_id=job_id,
client=client,

    ).parsed

async def asyncio_detailed(
    job_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[RhubapitowergetJobResponse200]:
    kwargs = _get_kwargs(
        job_id=job_id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    job_id: int,
    *,
    client: AuthenticatedClient,

) -> Optional[RhubapitowergetJobResponse200]:
    """  """

    return (await asyncio_detailed(
        job_id=job_id,
client=client,

    )).parsed
