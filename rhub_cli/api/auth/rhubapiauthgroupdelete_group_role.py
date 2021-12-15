from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthgroupdelete_group_role_json_body import RhubapiauthgroupdeleteGroupRoleJsonBody
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupdeleteGroupRoleJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/group/{group_id}/roles".format(client.base_url, group_id=group_id)

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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupdeleteGroupRoleJsonBody,
) -> Response[Any]:
    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupdeleteGroupRoleJsonBody,
) -> Response[Any]:
    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
