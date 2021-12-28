from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapitowerdelete_server_response_default import RhubapitowerdeleteServerResponseDefault
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapitowerdeleteServerResponseDefault]]:
    if response.status_code == 204:
        response_204 = None

        return response_204

    else:
        response_default = RhubapitowerdeleteServerResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapitowerdeleteServerResponseDefault]]:
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
) -> Response[Union[Any, RhubapitowerdeleteServerResponseDefault]]:
    """
    Args:
        server_id (int):

    Returns:
        Response[Union[Any, RhubapitowerdeleteServerResponseDefault]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapitowerdeleteServerResponseDefault]]:
    """
    Args:
        server_id (int):

    Returns:
        Response[Union[Any, RhubapitowerdeleteServerResponseDefault]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapitowerdeleteServerResponseDefault]]:
    """
    Args:
        server_id (int):

    Returns:
        Response[Union[Any, RhubapitowerdeleteServerResponseDefault]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapitowerdeleteServerResponseDefault]]:
    """
    Args:
        server_id (int):

    Returns:
        Response[Union[Any, RhubapitowerdeleteServerResponseDefault]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
        )
    ).parsed
