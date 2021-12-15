from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.rhubapitowerupdate_template_response_200 import RhubapitowerupdateTemplateResponse200
from typing import cast
from ...models.rhubapitowerupdate_template_json_body import RhubapitowerupdateTemplateJsonBody
from typing import Dict



def _get_kwargs(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerupdateTemplateJsonBody,

) -> Dict[str, Any]:
    url = "{}/tower/template/{template_id}".format(
        client.base_url,template_id=template_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[RhubapitowerupdateTemplateResponse200]:
    if response.status_code == 200:
        response_200 = RhubapitowerupdateTemplateResponse200.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapitowerupdateTemplateResponse200]:
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
    json_body: RhubapitowerupdateTemplateJsonBody,

) -> Response[RhubapitowerupdateTemplateResponse200]:
    kwargs = _get_kwargs(
        template_id=template_id,
client=client,
json_body=json_body,

    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerupdateTemplateJsonBody,

) -> Optional[RhubapitowerupdateTemplateResponse200]:
    """  """

    return sync_detailed(
        template_id=template_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerupdateTemplateJsonBody,

) -> Response[RhubapitowerupdateTemplateResponse200]:
    kwargs = _get_kwargs(
        template_id=template_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerupdateTemplateJsonBody,

) -> Optional[RhubapitowerupdateTemplateResponse200]:
    """  """

    return (await asyncio_detailed(
        template_id=template_id,
client=client,
json_body=json_body,

    )).parsed
