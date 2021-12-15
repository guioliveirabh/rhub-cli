from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapitowerget_server_response_200 import RhubapitowergetServerResponse200
from ...models.rhubapitowerget_server_response_default import RhubapitowergetServerResponseDefault
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubapitowergetServerResponse200, RhubapitowergetServerResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapitowergetServerResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapitowergetServerResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapitowergetServerResponse200, RhubapitowergetServerResponseDefault]]:
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
) -> Response[Union[RhubapitowergetServerResponse200, RhubapitowergetServerResponseDefault]]:
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
) -> Optional[Union[RhubapitowergetServerResponse200, RhubapitowergetServerResponseDefault]]:
    """ """

    return sync_detailed(
        server_id=server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubapitowergetServerResponse200, RhubapitowergetServerResponseDefault]]:
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
) -> Optional[Union[RhubapitowergetServerResponse200, RhubapitowergetServerResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
        )
    ).parsed
