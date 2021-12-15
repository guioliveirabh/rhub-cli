from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthgrouplist_group_users_response_200_item import RhubapiauthgrouplistGroupUsersResponse200Item
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/group/{group_id}/users".format(client.base_url, group_id=group_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[RhubapiauthgrouplistGroupUsersResponse200Item]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubapiauthgrouplistGroupUsersResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[RhubapiauthgrouplistGroupUsersResponse200Item]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List[RhubapiauthgrouplistGroupUsersResponse200Item]]:
    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List[RhubapiauthgrouplistGroupUsersResponse200Item]]:
    """See also [Keycloak API: UserRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List[RhubapiauthgrouplistGroupUsersResponse200Item]]:
    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List[RhubapiauthgrouplistGroupUsersResponse200Item]]:
    """See also [Keycloak API: UserRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
