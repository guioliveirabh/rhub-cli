from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthgroupcreate_group_json_body import RhubapiauthgroupcreateGroupJsonBody
from ...models.rhubapiauthgroupcreate_group_response_200 import RhubapiauthgroupcreateGroupResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupcreateGroupJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/group".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[RhubapiauthgroupcreateGroupResponse200]:
    if response.status_code == 200:
        response_200 = RhubapiauthgroupcreateGroupResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapiauthgroupcreateGroupResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupcreateGroupJsonBody,
) -> Response[RhubapiauthgroupcreateGroupResponse200]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupcreateGroupJsonBody,
) -> Optional[RhubapiauthgroupcreateGroupResponse200]:
    """Create a group in the database. Returns created group data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupcreateGroupJsonBody,
) -> Response[RhubapiauthgroupcreateGroupResponse200]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupcreateGroupJsonBody,
) -> Optional[RhubapiauthgroupcreateGroupResponse200]:
    """Create a group in the database. Returns created group data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
