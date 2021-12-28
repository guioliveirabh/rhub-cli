from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapitowerlaunch_template_json_body import RhubapitowerlaunchTemplateJsonBody
from ...models.rhubapitowerlaunch_template_response_200 import RhubapitowerlaunchTemplateResponse200
from ...models.rhubapitowerlaunch_template_response_default import RhubapitowerlaunchTemplateResponseDefault
from ...types import Response


def _get_kwargs(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerlaunchTemplateJsonBody,
) -> Dict[str, Any]:
    url = "{}/tower/template/{template_id}/launch".format(client.base_url, template_id=template_id)

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
) -> Optional[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapitowerlaunchTemplateResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapitowerlaunchTemplateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]:
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
    json_body: RhubapitowerlaunchTemplateJsonBody,
) -> Response[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]:
    """Launch Tower template

    Args:
        template_id (int):
        json_body (RhubapitowerlaunchTemplateJsonBody):

    Returns:
        Response[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerlaunchTemplateJsonBody,
) -> Optional[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]:
    """Launch Tower template

    Args:
        template_id (int):
        json_body (RhubapitowerlaunchTemplateJsonBody):

    Returns:
        Response[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerlaunchTemplateJsonBody,
) -> Response[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]:
    """Launch Tower template

    Args:
        template_id (int):
        json_body (RhubapitowerlaunchTemplateJsonBody):

    Returns:
        Response[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapitowerlaunchTemplateJsonBody,
) -> Optional[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]:
    """Launch Tower template

    Args:
        template_id (int):
        json_body (RhubapitowerlaunchTemplateJsonBody):

    Returns:
        Response[Union[RhubapitowerlaunchTemplateResponse200, RhubapitowerlaunchTemplateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
