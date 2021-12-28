from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapilabregioncreate_region_json_body import RhubapilabregioncreateRegionJsonBody
from ...models.rhubapilabregioncreate_region_response_default import RhubapilabregioncreateRegionResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregioncreateRegionJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/region".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapilabregioncreateRegionResponseDefault]]:
    if response.status_code == 200:
        response_200 = None

        return response_200

    else:
        response_default = RhubapilabregioncreateRegionResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapilabregioncreateRegionResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregioncreateRegionJsonBody,
) -> Response[Union[Any, RhubapilabregioncreateRegionResponseDefault]]:
    """Create region

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster)
    for more info how reservation, lifespan, and other properties affects clusters.

    `quota` and `lifespan` can be set to `null` to provide unlimited access
    to the region.

    `users_group` limits region to a selected group of users, if the value
    is `null` any user can use region.

    Args:
        json_body (RhubapilabregioncreateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubapilabregioncreateRegionResponseDefault]]
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
    json_body: RhubapilabregioncreateRegionJsonBody,
) -> Optional[Union[Any, RhubapilabregioncreateRegionResponseDefault]]:
    """Create region

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster)
    for more info how reservation, lifespan, and other properties affects clusters.

    `quota` and `lifespan` can be set to `null` to provide unlimited access
    to the region.

    `users_group` limits region to a selected group of users, if the value
    is `null` any user can use region.

    Args:
        json_body (RhubapilabregioncreateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubapilabregioncreateRegionResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapilabregioncreateRegionJsonBody,
) -> Response[Union[Any, RhubapilabregioncreateRegionResponseDefault]]:
    """Create region

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster)
    for more info how reservation, lifespan, and other properties affects clusters.

    `quota` and `lifespan` can be set to `null` to provide unlimited access
    to the region.

    `users_group` limits region to a selected group of users, if the value
    is `null` any user can use region.

    Args:
        json_body (RhubapilabregioncreateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubapilabregioncreateRegionResponseDefault]]
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
    json_body: RhubapilabregioncreateRegionJsonBody,
) -> Optional[Union[Any, RhubapilabregioncreateRegionResponseDefault]]:
    """Create region

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster)
    for more info how reservation, lifespan, and other properties affects clusters.

    `quota` and `lifespan` can be set to `null` to provide unlimited access
    to the region.

    `users_group` limits region to a selected group of users, if the value
    is `null` any user can use region.

    Args:
        json_body (RhubapilabregioncreateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubapilabregioncreateRegionResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
