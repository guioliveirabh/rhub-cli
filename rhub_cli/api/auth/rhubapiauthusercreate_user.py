from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthusercreate_user_json_body import RhubapiauthusercreateUserJsonBody
from ...models.rhubapiauthusercreate_user_response_200 import RhubapiauthusercreateUserResponse200
from ...models.rhubapiauthusercreate_user_response_default import RhubapiauthusercreateUserResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthusercreateUserJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/user".format(client.base_url)

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
) -> Optional[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapiauthusercreateUserResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapiauthusercreateUserResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthusercreateUserJsonBody,
) -> Response[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]:
    """Create user

     Create a user in the database. Returns created user data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        json_body (RhubapiauthusercreateUserJsonBody):

    Returns:
        Response[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]
    """

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
    json_body: RhubapiauthusercreateUserJsonBody,
) -> Optional[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]:
    """Create user

     Create a user in the database. Returns created user data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        json_body (RhubapiauthusercreateUserJsonBody):

    Returns:
        Response[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapiauthusercreateUserJsonBody,
) -> Response[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]:
    """Create user

     Create a user in the database. Returns created user data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        json_body (RhubapiauthusercreateUserJsonBody):

    Returns:
        Response[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]
    """

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
    json_body: RhubapiauthusercreateUserJsonBody,
) -> Optional[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]:
    """Create user

     Create a user in the database. Returns created user data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        json_body (RhubapiauthusercreateUserJsonBody):

    Returns:
        Response[Union[RhubapiauthusercreateUserResponse200, RhubapiauthusercreateUserResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
