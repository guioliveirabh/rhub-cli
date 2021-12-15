from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import cast
from ...models.rhubapitowerwebhook_notification_json_body import RhubapitowerwebhookNotificationJsonBody
from typing import Dict



def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerwebhookNotificationJsonBody,

) -> Dict[str, Any]:
    url = "{}/tower/webhook_notification".format(
        client.base_url)

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




def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerwebhookNotificationJsonBody,

) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerwebhookNotificationJsonBody,

) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(
            **kwargs
        )

    return _build_response(response=response)

