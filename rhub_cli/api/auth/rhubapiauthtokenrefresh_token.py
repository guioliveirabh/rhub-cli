from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.rhubapiauthtokenrefresh_token_response_200 import RhubapiauthtokenrefreshTokenResponse200
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    client: Client,
    authorization: str,

) -> Dict[str, Any]:
    url = "{}/auth/token/refresh".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["authorization"] = authorization


    

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RhubapiauthtokenrefreshTokenResponse200]:
    if response.status_code == 200:
        response_200 = RhubapiauthtokenrefreshTokenResponse200.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapiauthtokenrefreshTokenResponse200]:
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

) -> Response[RhubapiauthtokenrefreshTokenResponse200]:
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

) -> Optional[RhubapiauthtokenrefreshTokenResponse200]:
    """ This endpoint requires HTTP bearer authentication. The bearer token in
'Authorization' header is not access token but refresh token. If refresh
was successful return new oauth2 token info. Response is the same as
from token create endpoint.
 """

    return sync_detailed(
        client=client,
authorization=authorization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    authorization: str,

) -> Response[RhubapiauthtokenrefreshTokenResponse200]:
    kwargs = _get_kwargs(
        client=client,
authorization=authorization,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    authorization: str,

) -> Optional[RhubapiauthtokenrefreshTokenResponse200]:
    """ This endpoint requires HTTP bearer authentication. The bearer token in
'Authorization' header is not access token but refresh token. If refresh
was successful return new oauth2 token info. Response is the same as
from token create endpoint.
 """

    return (await asyncio_detailed(
        client=client,
authorization=authorization,

    )).parsed
