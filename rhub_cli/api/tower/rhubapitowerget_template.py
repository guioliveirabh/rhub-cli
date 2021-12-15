from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import cast
from ...models.rhubapitowerget_template_response_200 import RhubapitowergetTemplateResponse200
from typing import Dict



def _get_kwargs(
    template_id: int,
    *,
    client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/tower/template/{template_id}".format(
        client.base_url,template_id=template_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RhubapitowergetTemplateResponse200]:
    if response.status_code == 200:
        response_200 = RhubapitowergetTemplateResponse200.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapitowergetTemplateResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    template_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[RhubapitowergetTemplateResponse200]:
    kwargs = _get_kwargs(
        template_id=template_id,
client=client,

    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    template_id: int,
    *,
    client: AuthenticatedClient,

) -> Optional[RhubapitowergetTemplateResponse200]:
    """  """

    return sync_detailed(
        template_id=template_id,
client=client,

    ).parsed

async def asyncio_detailed(
    template_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[RhubapitowergetTemplateResponse200]:
    kwargs = _get_kwargs(
        template_id=template_id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    template_id: int,
    *,
    client: AuthenticatedClient,

) -> Optional[RhubapitowergetTemplateResponse200]:
    """  """

    return (await asyncio_detailed(
        template_id=template_id,
client=client,

    )).parsed
