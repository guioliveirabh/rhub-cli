from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapipoliciescreate_policy_json_body import RhubapipoliciescreatePolicyJsonBody
from ...models.rhubapipoliciescreate_policy_response_200 import RhubapipoliciescreatePolicyResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubapipoliciescreatePolicyJsonBody,
) -> Dict[str, Any]:
    url = "{}/policies".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[RhubapipoliciescreatePolicyResponse200]:
    if response.status_code == 200:
        response_200 = RhubapipoliciescreatePolicyResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RhubapipoliciescreatePolicyResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapipoliciescreatePolicyJsonBody,
) -> Response[RhubapipoliciescreatePolicyResponse200]:
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
    json_body: RhubapipoliciescreatePolicyJsonBody,
) -> Optional[RhubapipoliciescreatePolicyResponse200]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubapipoliciescreatePolicyJsonBody,
) -> Response[RhubapipoliciescreatePolicyResponse200]:
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
    json_body: RhubapipoliciescreatePolicyJsonBody,
) -> Optional[RhubapipoliciescreatePolicyResponse200]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
