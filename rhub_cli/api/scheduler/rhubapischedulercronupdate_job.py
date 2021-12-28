from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapischedulercronupdate_job_json_body import RhubapischedulercronupdateJobJsonBody
from ...models.rhubapischedulercronupdate_job_response_200 import RhubapischedulercronupdateJobResponse200
from ...models.rhubapischedulercronupdate_job_response_default import RhubapischedulercronupdateJobResponseDefault
from ...types import Response


def _get_kwargs(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapischedulercronupdateJobJsonBody,
) -> Dict[str, Any]:
    url = "{}/scheduler/cron/{cron_job_id}".format(client.base_url, cron_job_id=cron_job_id)

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
) -> Optional[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapischedulercronupdateJobResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapischedulercronupdateJobResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]:
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
    json_body: RhubapischedulercronupdateJobJsonBody,
) -> Response[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]:
    """Update CronJob

    Args:
        cron_job_id (int):
        json_body (RhubapischedulercronupdateJobJsonBody):

    Returns:
        Response[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]
    """

    kwargs = _get_kwargs(
        cron_job_id=cron_job_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapischedulercronupdateJobJsonBody,
) -> Optional[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]:
    """Update CronJob

    Args:
        cron_job_id (int):
        json_body (RhubapischedulercronupdateJobJsonBody):

    Returns:
        Response[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]
    """

    return sync_detailed(
        cron_job_id=cron_job_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapischedulercronupdateJobJsonBody,
) -> Response[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]:
    """Update CronJob

    Args:
        cron_job_id (int):
        json_body (RhubapischedulercronupdateJobJsonBody):

    Returns:
        Response[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]
    """

    kwargs = _get_kwargs(
        cron_job_id=cron_job_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapischedulercronupdateJobJsonBody,
) -> Optional[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]:
    """Update CronJob

    Args:
        cron_job_id (int):
        json_body (RhubapischedulercronupdateJobJsonBody):

    Returns:
        Response[Union[RhubapischedulercronupdateJobResponse200, RhubapischedulercronupdateJobResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cron_job_id=cron_job_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
