from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapiauthuserget_current_user_response_200 import RhubapiauthusergetCurrentUserResponse200
from ...models.rhubapiauthuserget_current_user_response_default import RhubapiauthusergetCurrentUserResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/me".format(client.base_url)

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
) -> Optional[Union[RhubapiauthusergetCurrentUserResponse200, RhubapiauthusergetCurrentUserResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapiauthusergetCurrentUserResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapiauthusergetCurrentUserResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapiauthusergetCurrentUserResponse200, RhubapiauthusergetCurrentUserResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubapiauthusergetCurrentUserResponse200, RhubapiauthusergetCurrentUserResponseDefault]]:
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
) -> Optional[Union[RhubapiauthusergetCurrentUserResponse200, RhubapiauthusergetCurrentUserResponseDefault]]:
    """ """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubapiauthusergetCurrentUserResponse200, RhubapiauthusergetCurrentUserResponseDefault]]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubapiauthusergetCurrentUserResponse200, RhubapiauthusergetCurrentUserResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
