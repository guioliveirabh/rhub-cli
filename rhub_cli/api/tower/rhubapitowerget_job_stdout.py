from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapitowerget_job_stdout_response_default import RhubapitowergetJobStdoutResponseDefault
from ...types import Response


def _get_kwargs(
    job_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/tower/job/{job_id}/stdout".format(client.base_url, job_id=job_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[RhubapitowergetJobStdoutResponseDefault, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.text)
        return response_200

    else:
        response_default = RhubapitowergetJobStdoutResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[RhubapitowergetJobStdoutResponseDefault, str]]:
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
) -> Response[Union[RhubapitowergetJobStdoutResponseDefault, str]]:
    """Get stdout of Tower job

    Args:
        job_id (int):

    Returns:
        Response[Union[RhubapitowergetJobStdoutResponseDefault, str]]
    """

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
) -> Optional[Union[RhubapitowergetJobStdoutResponseDefault, str]]:
    """Get stdout of Tower job

    Args:
        job_id (int):

    Returns:
        Response[Union[RhubapitowergetJobStdoutResponseDefault, str]]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubapitowergetJobStdoutResponseDefault, str]]:
    """Get stdout of Tower job

    Args:
        job_id (int):

    Returns:
        Response[Union[RhubapitowergetJobStdoutResponseDefault, str]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    job_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubapitowergetJobStdoutResponseDefault, str]]:
    """Get stdout of Tower job

    Args:
        job_id (int):

    Returns:
        Response[Union[RhubapitowergetJobStdoutResponseDefault, str]]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
