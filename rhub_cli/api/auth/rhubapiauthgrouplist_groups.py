from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthgrouplist_groups_response_200_item import RhubapiauthgrouplistGroupsResponse200Item
from ...models.rhubapiauthgrouplist_groups_response_default import RhubapiauthgrouplistGroupsResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/group".format(client.base_url)

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
) -> Optional[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubapiauthgrouplistGroupsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubapiauthgrouplistGroupsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]:
    """Get group list

     See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Returns:
        Response[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]:
    """Get group list

     See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Returns:
        Response[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]:
    """Get group list

     See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Returns:
        Response[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]:
    """Get group list

     See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Returns:
        Response[Union[List[RhubapiauthgrouplistGroupsResponse200Item], RhubapiauthgrouplistGroupsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
