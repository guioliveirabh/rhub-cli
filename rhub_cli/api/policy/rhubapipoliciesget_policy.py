from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapipoliciesget_policy_response_200 import RhubapipoliciesgetPolicyResponse200
from ...models.rhubapipoliciesget_policy_response_default import RhubapipoliciesgetPolicyResponseDefault
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, RhubapipoliciesgetPolicyResponse200, RhubapipoliciesgetPolicyResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapipoliciesgetPolicyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = None

        return response_404

    else:
        response_default = RhubapipoliciesgetPolicyResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubapipoliciesgetPolicyResponse200, RhubapipoliciesgetPolicyResponseDefault]]:
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
) -> Response[Union[Any, RhubapipoliciesgetPolicyResponse200, RhubapipoliciesgetPolicyResponseDefault]]:
    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapipoliciesgetPolicyResponse200, RhubapipoliciesgetPolicyResponseDefault]]:
    """ """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubapipoliciesgetPolicyResponse200, RhubapipoliciesgetPolicyResponseDefault]]:
    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubapipoliciesgetPolicyResponse200, RhubapipoliciesgetPolicyResponseDefault]]:
    """ """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
        )
    ).parsed
