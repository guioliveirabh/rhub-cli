from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthgroupadd_group_role_json_body import RhubapiauthgroupaddGroupRoleJsonBody
from ...models.rhubapiauthgroupadd_group_role_response_default import RhubapiauthgroupaddGroupRoleResponseDefault
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupaddGroupRoleJsonBody,
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]:
    if response.status_code == 200:
        response_200 = None

        return response_200

    else:
        response_default = RhubapiauthgroupaddGroupRoleResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]:
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
    json_body: RhubapiauthgroupaddGroupRoleJsonBody,
) -> Response[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]:
    """Add group to role

    Args:
        group_id (str):
        json_body (RhubapiauthgroupaddGroupRoleJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupaddGroupRoleJsonBody,
) -> Optional[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]:
    """Add group to role

    Args:
        group_id (str):
        json_body (RhubapiauthgroupaddGroupRoleJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]
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
    json_body: RhubapiauthgroupaddGroupRoleJsonBody,
) -> Response[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]:
    """Add group to role

    Args:
        group_id (str):
        json_body (RhubapiauthgroupaddGroupRoleJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthgroupaddGroupRoleJsonBody,
) -> Optional[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]:
    """Add group to role

    Args:
        group_id (str):
        json_body (RhubapiauthgroupaddGroupRoleJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthgroupaddGroupRoleResponseDefault]]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
