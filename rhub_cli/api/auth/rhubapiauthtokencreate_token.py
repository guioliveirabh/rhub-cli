from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.rhubapiauthtokencreate_token_response_200 import RhubapiauthtokencreateTokenResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    authorization: str,
) -> Dict[str, Any]:
    url = "{}/auth/token/create".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["authorization"] = authorization

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RhubapiauthtokencreateTokenResponse200]:
    if response.status_code == 200:
        response_200 = RhubapiauthtokencreateTokenResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapiauthtokencreateTokenResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    authorization: str,
) -> Response[RhubapiauthtokencreateTokenResponse200]:
    kwargs = _get_kwargs(
        client=client,
        authorization=authorization,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    authorization: str,
) -> Optional[RhubapiauthtokencreateTokenResponse200]:
    """This endpoint requires HTTP basic authentication. If credentials are
    correct then it returns oauth2 token info - access token, refresh token
    and some other informations about generated token.
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    authorization: str,
) -> Response[RhubapiauthtokencreateTokenResponse200]:
    kwargs = _get_kwargs(
        client=client,
        authorization=authorization,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    authorization: str,
) -> Optional[RhubapiauthtokencreateTokenResponse200]:
    """This endpoint requires HTTP basic authentication. If credentials are
    correct then it returns oauth2 token info - access token, refresh token
    and some other informations about generated token.
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
