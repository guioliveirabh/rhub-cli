from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.rhub_api_bare_metal_provision_provision_get_kickstart_response_default import (
    RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault,
)
from ...types import Response


def _get_kwargs(
    provision_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/bare_metal/provision/{provision_id}/kickstart".format(client.base_url, provision_id=provision_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.text)
        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    else:
        response_default = RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    provision_id: int,
    *,
    client: Client,
) -> Response[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]:
    """Get provision's kickstart file

    Args:
        provision_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]
    """

    kwargs = _get_kwargs(
        provision_id=provision_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    provision_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]:
    """Get provision's kickstart file

    Args:
        provision_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]
    """

    return sync_detailed(
        provision_id=provision_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    provision_id: int,
    *,
    client: Client,
) -> Response[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]:
    """Get provision's kickstart file

    Args:
        provision_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]
    """

    kwargs = _get_kwargs(
        provision_id=provision_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    provision_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]:
    """Get provision's kickstart file

    Args:
        provision_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionGetKickstartResponseDefault, str]]
    """

    return (
        await asyncio_detailed(
            provision_id=provision_id,
            client=client,
        )
    ).parsed
