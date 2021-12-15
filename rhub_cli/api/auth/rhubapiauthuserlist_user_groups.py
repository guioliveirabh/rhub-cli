from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthuserlist_user_groups_response_200_item import RhubapiauthuserlistUserGroupsResponse200Item
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}/groups".format(client.base_url, user_id=user_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[RhubapiauthuserlistUserGroupsResponse200Item]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubapiauthuserlistUserGroupsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[RhubapiauthuserlistUserGroupsResponse200Item]]:
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
) -> Response[List[RhubapiauthuserlistUserGroupsResponse200Item]]:
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
) -> Optional[List[RhubapiauthuserlistUserGroupsResponse200Item]]:
    """See also [Keycloak API: GroupRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List[RhubapiauthuserlistUserGroupsResponse200Item]]:
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
) -> Optional[List[RhubapiauthuserlistUserGroupsResponse200Item]]:
    """See also [Keycloak API: GroupRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
