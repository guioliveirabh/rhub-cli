from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET




def _get_kwargs(
    server_id: int,
    *,
    client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/tower/server/{server_id}".format(
        client.base_url,server_id=server_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }




def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    kwargs = _get_kwargs(
        server_id=server_id,
client=client,

    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    kwargs = _get_kwargs(
        server_id=server_id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(
            **kwargs
        )

    return _build_response(response=response)

