from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapipoliciesdelete_policy_response_default import RhubapipoliciesdeletePolicyResponseDefault
from ...types import Response


def _get_kwargs(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/policies/{policy_id}".format(client.base_url, policy_id=policy_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubapipoliciesdeletePolicyResponseDefault]]:
    if response.status_code == 204:
        response_204 = None

        return response_204

    else:
        response_default = RhubapipoliciesdeletePolicyResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubapipoliciesdeletePolicyResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapipoliciesdeletePolicyResponseDefault]]:
    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapipoliciesdeletePolicyResponseDefault]]:
    """ """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapipoliciesdeletePolicyResponseDefault]]:
    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapipoliciesdeletePolicyResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
        )
    ).parsed
