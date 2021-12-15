from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthuserlist_user_roles_response_200_item import RhubapiauthuserlistUserRolesResponse200Item
from ...models.rhubapiauthuserlist_user_roles_response_default import RhubapiauthuserlistUserRolesResponseDefault
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}/roles".format(client.base_url, user_id=user_id)

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
) -> Optional[Union[List[RhubapiauthuserlistUserRolesResponse200Item], RhubapiauthuserlistUserRolesResponseDefault]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubapiauthuserlistUserRolesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubapiauthuserlistUserRolesResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[List[RhubapiauthuserlistUserRolesResponse200Item], RhubapiauthuserlistUserRolesResponseDefault]]:
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
) -> Response[Union[List[RhubapiauthuserlistUserRolesResponse200Item], RhubapiauthuserlistUserRolesResponseDefault]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[List[RhubapiauthuserlistUserRolesResponse200Item], RhubapiauthuserlistUserRolesResponseDefault]]:
    """ """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[List[RhubapiauthuserlistUserRolesResponse200Item], RhubapiauthuserlistUserRolesResponseDefault]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[List[RhubapiauthuserlistUserRolesResponse200Item], RhubapiauthuserlistUserRolesResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
