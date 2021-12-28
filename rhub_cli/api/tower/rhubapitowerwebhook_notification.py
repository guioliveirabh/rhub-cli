from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapitowerwebhook_notification_json_body import RhubapitowerwebhookNotificationJsonBody
from ...models.rhubapitowerwebhook_notification_response_default import RhubapitowerwebhookNotificationResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerwebhookNotificationJsonBody,
) -> Dict[str, Any]:
    url = "{}/tower/webhook_notification".format(client.base_url)

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
) -> Optional[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]:
    if response.status_code == 204:
        response_204 = None

        return response_204

    else:
        response_default = RhubapitowerwebhookNotificationResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerwebhookNotificationJsonBody,
) -> Response[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubapitowerwebhookNotificationJsonBody):

    Returns:
        Response[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]
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
    json_body: RhubapitowerwebhookNotificationJsonBody,
) -> Optional[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubapitowerwebhookNotificationJsonBody):

    Returns:
        Response[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerwebhookNotificationJsonBody,
) -> Response[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubapitowerwebhookNotificationJsonBody):

    Returns:
        Response[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]
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
    json_body: RhubapitowerwebhookNotificationJsonBody,
) -> Optional[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubapitowerwebhookNotificationJsonBody):

    Returns:
        Response[Union[Any, RhubapitowerwebhookNotificationResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
