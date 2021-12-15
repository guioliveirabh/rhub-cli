from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthgroupget_group_response_200 import RhubapiauthgroupgetGroupResponse200
from ...models.rhubapiauthgroupget_group_response_default import RhubapiauthgroupgetGroupResponseDefault
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/group/{group_id}".format(client.base_url, group_id=group_id)

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
) -> Optional[Union[RhubapiauthgroupgetGroupResponse200, RhubapiauthgroupgetGroupResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapiauthgroupgetGroupResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapiauthgroupgetGroupResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapiauthgroupgetGroupResponse200, RhubapiauthgroupgetGroupResponseDefault]]:
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
) -> Response[Union[RhubapiauthgroupgetGroupResponse200, RhubapiauthgroupgetGroupResponseDefault]]:
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
) -> Optional[Union[RhubapiauthgroupgetGroupResponse200, RhubapiauthgroupgetGroupResponseDefault]]:
    """Returns group data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `subGroups` and others.

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubapiauthgroupgetGroupResponse200, RhubapiauthgroupgetGroupResponseDefault]]:
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
) -> Optional[Union[RhubapiauthgroupgetGroupResponse200, RhubapiauthgroupgetGroupResponseDefault]]:
    """Returns group data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `subGroups` and others.

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
