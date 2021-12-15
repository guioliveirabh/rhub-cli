from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthuserget_user_response_200 import RhubapiauthusergetUserResponse200
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}".format(client.base_url, user_id=user_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RhubapiauthusergetUserResponse200]:
    if response.status_code == 200:
        response_200 = RhubapiauthusergetUserResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapiauthusergetUserResponse200]:
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
) -> Response[RhubapiauthusergetUserResponse200]:
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
) -> Optional[RhubapiauthusergetUserResponse200]:
    """Returns user data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `createdTimestamp` and others.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[RhubapiauthusergetUserResponse200]:
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
) -> Optional[RhubapiauthusergetUserResponse200]:
    """Returns user data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `createdTimestamp` and others.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
