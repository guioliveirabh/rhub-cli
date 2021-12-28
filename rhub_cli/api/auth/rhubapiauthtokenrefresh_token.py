from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.rhubapiauthtokenrefresh_token_response_200 import RhubapiauthtokenrefreshTokenResponse200
from ...models.rhubapiauthtokenrefresh_token_response_default import RhubapiauthtokenrefreshTokenResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    authorization: str,
) -> Dict[str, Any]:
    url = "{}/auth/token/refresh".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["authorization"] = authorization

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapiauthtokenrefreshTokenResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapiauthtokenrefreshTokenResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]:
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
) -> Response[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]:
    """Refresh token

     This endpoint requires HTTP bearer authentication. The bearer token in
    'Authorization' header is not access token but refresh token. If refresh
    was successful return new oauth2 token info. Response is the same as
    from token create endpoint.

    Args:
        authorization (str):  Example: Bearer eyJhbGciOiJIUzI1...VLzc.

    Returns:
        Response[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]
    """

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
) -> Optional[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]:
    """Refresh token

     This endpoint requires HTTP bearer authentication. The bearer token in
    'Authorization' header is not access token but refresh token. If refresh
    was successful return new oauth2 token info. Response is the same as
    from token create endpoint.

    Args:
        authorization (str):  Example: Bearer eyJhbGciOiJIUzI1...VLzc.

    Returns:
        Response[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    authorization: str,
) -> Response[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]:
    """Refresh token

     This endpoint requires HTTP bearer authentication. The bearer token in
    'Authorization' header is not access token but refresh token. If refresh
    was successful return new oauth2 token info. Response is the same as
    from token create endpoint.

    Args:
        authorization (str):  Example: Bearer eyJhbGciOiJIUzI1...VLzc.

    Returns:
        Response[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]
    """

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
) -> Optional[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]:
    """Refresh token

     This endpoint requires HTTP bearer authentication. The bearer token in
    'Authorization' header is not access token but refresh token. If refresh
    was successful return new oauth2 token info. Response is the same as
    from token create endpoint.

    Args:
        authorization (str):  Example: Bearer eyJhbGciOiJIUzI1...VLzc.

    Returns:
        Response[Union[RhubapiauthtokenrefreshTokenResponse200, RhubapiauthtokenrefreshTokenResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
