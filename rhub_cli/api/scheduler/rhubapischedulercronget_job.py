from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapischedulercronget_job_response_200 import RhubapischedulercrongetJobResponse200
from ...models.rhubapischedulercronget_job_response_default import RhubapischedulercrongetJobResponseDefault
from ...types import Response


def _get_kwargs(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/scheduler/cron/{cron_job_id}".format(client.base_url, cron_job_id=cron_job_id)

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
) -> Optional[Union[RhubapischedulercrongetJobResponse200, RhubapischedulercrongetJobResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapischedulercrongetJobResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapischedulercrongetJobResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapischedulercrongetJobResponse200, RhubapischedulercrongetJobResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubapischedulercrongetJobResponse200, RhubapischedulercrongetJobResponseDefault]]:
    kwargs = _get_kwargs(
        cron_job_id=cron_job_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubapischedulercrongetJobResponse200, RhubapischedulercrongetJobResponseDefault]]:
    """ """

    return sync_detailed(
        cron_job_id=cron_job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubapischedulercrongetJobResponse200, RhubapischedulercrongetJobResponseDefault]]:
    kwargs = _get_kwargs(
        cron_job_id=cron_job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubapischedulercrongetJobResponse200, RhubapischedulercrongetJobResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            cron_job_id=cron_job_id,
            client=client,
        )
    ).parsed
