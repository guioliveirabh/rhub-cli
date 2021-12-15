from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapitowerget_server_response_200 import RhubapitowergetServerResponse200
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/tower/server/{server_id}".format(client.base_url, server_id=server_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RhubapitowergetServerResponse200]:
    if response.status_code == 200:
        response_200 = RhubapitowergetServerResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapitowergetServerResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[RhubapitowergetServerResponse200]:
    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[RhubapitowergetServerResponse200]:
    """ """

    return sync_detailed(
        server_id=server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[RhubapitowergetServerResponse200]:
    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[RhubapitowergetServerResponse200]:
    """ """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
        )
    ).parsed
