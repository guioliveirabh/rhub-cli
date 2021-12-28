from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabclusterget_cluster_event_stdout_response_default import (
    RhubapilabclustergetClusterEventStdoutResponseDefault,
)
from ...types import Response


def _get_kwargs(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/cluster_event/{event_id}/stdout".format(client.base_url, event_id=event_id)

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
) -> Optional[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.text)
        return response_200

    else:
        response_default = RhubapilabclustergetClusterEventStdoutResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]:
    """Get cluster event output

    Args:
        event_id (int):

    Returns:
        Response[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]:
    """Get cluster event output

    Args:
        event_id (int):

    Returns:
        Response[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]:
    """Get cluster event output

    Args:
        event_id (int):

    Returns:
        Response[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]:
    """Get cluster event output

    Args:
        event_id (int):

    Returns:
        Response[Union[RhubapilabclustergetClusterEventStdoutResponseDefault, str]]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
        )
    ).parsed
