from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthuserdelete_user_response_default import RhubapiauthuserdeleteUserResponseDefault
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}".format(client.base_url, user_id=user_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]:
    if response.status_code == 200:
        response_200 = None

        return response_200

    else:
        response_default = RhubapiauthuserdeleteUserResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]:
    """Delete user

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]:
    """Delete user

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]:
    """Delete user

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]:
    """Delete user

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, RhubapiauthuserdeleteUserResponseDefault]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
