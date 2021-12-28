from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthgroupdelete_group_role_json_body import RhubapiauthgroupdeleteGroupRoleJsonBody
from ...models.rhubapiauthgroupdelete_group_role_response_default import RhubapiauthgroupdeleteGroupRoleResponseDefault
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]:
    if response.status_code == 200:
        response_200 = None

        return response_200

    else:
        response_default = RhubapiauthgroupdeleteGroupRoleResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]:
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
    json_body: RhubapiauthgroupdeleteGroupRoleJsonBody,
) -> Response[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]:
    """Remove group from role

    Args:
        group_id (str):
        json_body (RhubapiauthgroupdeleteGroupRoleJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]
    """

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


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupdeleteGroupRoleJsonBody,
) -> Optional[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]:
    """Remove group from role

    Args:
        group_id (str):
        json_body (RhubapiauthgroupdeleteGroupRoleJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupdeleteGroupRoleJsonBody,
) -> Response[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]:
    """Remove group from role

    Args:
        group_id (str):
        json_body (RhubapiauthgroupdeleteGroupRoleJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupdeleteGroupRoleJsonBody,
) -> Optional[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]:
    """Remove group from role

    Args:
        group_id (str):
        json_body (RhubapiauthgroupdeleteGroupRoleJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthgroupdeleteGroupRoleResponseDefault]]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
