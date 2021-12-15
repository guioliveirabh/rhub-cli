from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabclusterget_cluster_event_response_default import (
    RhubapilabclustergetClusterEventResponseDefault,
)
from ...types import Response


def _get_kwargs(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/cluster_event/{event_id}".format(client.base_url, event_id=event_id)

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
) -> Optional[Union[Any, RhubapilabclustergetClusterEventResponseDefault]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Any:
            response_200_type_0 = data

            return response_200_type_0
            response_200_type_1 = data

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    else:
        response_default = RhubapilabclustergetClusterEventResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubapilabclustergetClusterEventResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapilabclustergetClusterEventResponseDefault]]:
    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapilabclustergetClusterEventResponseDefault]]:
    """ """

    return sync_detailed(
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapilabclustergetClusterEventResponseDefault]]:
    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapilabclustergetClusterEventResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
        )
    ).parsed
