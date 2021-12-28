from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthuserdelete_user_group_json_body import RhubapiauthuserdeleteUserGroupJsonBody
from ...models.rhubapiauthuserdelete_user_group_response_default import RhubapiauthuserdeleteUserGroupResponseDefault
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserdeleteUserGroupJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}/groups".format(client.base_url, user_id=user_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]:
    if response.status_code == 200:
        response_200 = None

        return response_200

    else:
        response_default = RhubapiauthuserdeleteUserGroupResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]:
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
    json_body: RhubapiauthuserdeleteUserGroupJsonBody,
) -> Response[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]:
    """Remove user from group

    Args:
        user_id (str):
        json_body (RhubapiauthuserdeleteUserGroupJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
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
    json_body: RhubapiauthuserdeleteUserGroupJsonBody,
) -> Optional[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]:
    """Remove user from group

    Args:
        user_id (str):
        json_body (RhubapiauthuserdeleteUserGroupJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserdeleteUserGroupJsonBody,
) -> Response[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]:
    """Remove user from group

    Args:
        user_id (str):
        json_body (RhubapiauthuserdeleteUserGroupJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthuserdeleteUserGroupJsonBody,
) -> Optional[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]:
    """Remove user from group

    Args:
        user_id (str):
        json_body (RhubapiauthuserdeleteUserGroupJsonBody):

    Returns:
        Response[Union[Any, RhubapiauthuserdeleteUserGroupResponseDefault]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
