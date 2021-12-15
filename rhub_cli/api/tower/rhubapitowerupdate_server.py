from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapitowerupdate_server_json_body import RhubapitowerupdateServerJsonBody
from ...models.rhubapitowerupdate_server_response_200 import RhubapitowerupdateServerResponse200
from ...models.rhubapitowerupdate_server_response_default import RhubapitowerupdateServerResponseDefault
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerupdateServerJsonBody,
) -> Dict[str, Any]:
    url = "{}/tower/server/{server_id}".format(client.base_url, server_id=server_id)

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
) -> Optional[Union[RhubapitowerupdateServerResponse200, RhubapitowerupdateServerResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapitowerupdateServerResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapitowerupdateServerResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapitowerupdateServerResponse200, RhubapitowerupdateServerResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerupdateServerJsonBody,
) -> Response[Union[RhubapitowerupdateServerResponse200, RhubapitowerupdateServerResponseDefault]]:
    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    server_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerupdateServerJsonBody,
) -> Optional[Union[RhubapitowerupdateServerResponse200, RhubapitowerupdateServerResponseDefault]]:
    """ """

    return sync_detailed(
        server_id=server_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerupdateServerJsonBody,
) -> Response[Union[RhubapitowerupdateServerResponse200, RhubapitowerupdateServerResponseDefault]]:
    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerupdateServerJsonBody,
) -> Optional[Union[RhubapitowerupdateServerResponse200, RhubapitowerupdateServerResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
