from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabclusterreboot_hosts_json_body import RhubapilabclusterrebootHostsJsonBody
from ...models.rhubapilabclusterreboot_hosts_response_200_item import RhubapilabclusterrebootHostsResponse200Item
from ...models.rhubapilabclusterreboot_hosts_response_default import RhubapilabclusterrebootHostsResponseDefault
from ...types import Response


def _get_kwargs(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabclusterrebootHostsJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/cluster/{cluster_id}/reboot".format(client.base_url, cluster_id=cluster_id)

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
) -> Optional[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubapilabclusterrebootHostsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubapilabclusterrebootHostsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabclusterrebootHostsJsonBody,
) -> Response[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]:
    """Reboot cluster hosts

     **Trigger** hosts reboot in OpenStack. You can soft or hard reboot a host.
    A soft reboot attempts a graceful shut down and restart of the host. A
    hard reboot power cycles the host.

    Only hosts that belong to the selected cluster can be rebooted, other
    hosts are silently ignored. A list of rebooted hosts is returned in the
    response body so you can verify which hosts will be rebooted.

    Args:
        cluster_id (int):
        json_body (RhubapilabclusterrebootHostsJsonBody):

    Returns:
        Response[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabclusterrebootHostsJsonBody,
) -> Optional[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]:
    """Reboot cluster hosts

     **Trigger** hosts reboot in OpenStack. You can soft or hard reboot a host.
    A soft reboot attempts a graceful shut down and restart of the host. A
    hard reboot power cycles the host.

    Only hosts that belong to the selected cluster can be rebooted, other
    hosts are silently ignored. A list of rebooted hosts is returned in the
    response body so you can verify which hosts will be rebooted.

    Args:
        cluster_id (int):
        json_body (RhubapilabclusterrebootHostsJsonBody):

    Returns:
        Response[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabclusterrebootHostsJsonBody,
) -> Response[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]:
    """Reboot cluster hosts

     **Trigger** hosts reboot in OpenStack. You can soft or hard reboot a host.
    A soft reboot attempts a graceful shut down and restart of the host. A
    hard reboot power cycles the host.

    Only hosts that belong to the selected cluster can be rebooted, other
    hosts are silently ignored. A list of rebooted hosts is returned in the
    response body so you can verify which hosts will be rebooted.

    Args:
        cluster_id (int):
        json_body (RhubapilabclusterrebootHostsJsonBody):

    Returns:
        Response[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabclusterrebootHostsJsonBody,
) -> Optional[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]:
    """Reboot cluster hosts

     **Trigger** hosts reboot in OpenStack. You can soft or hard reboot a host.
    A soft reboot attempts a graceful shut down and restart of the host. A
    hard reboot power cycles the host.

    Only hosts that belong to the selected cluster can be rebooted, other
    hosts are silently ignored. A list of rebooted hosts is returned in the
    response body so you can verify which hosts will be rebooted.

    Args:
        cluster_id (int):
        json_body (RhubapilabclusterrebootHostsJsonBody):

    Returns:
        Response[Union[List[RhubapilabclusterrebootHostsResponse200Item], RhubapilabclusterrebootHostsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
