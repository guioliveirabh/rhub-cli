from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhubapipoliciesupdate_policy_json_body import RhubapipoliciesupdatePolicyJsonBody
from ...models.rhubapipoliciesupdate_policy_response_200 import RhubapipoliciesupdatePolicyResponse200
from ...models.rhubapipoliciesupdate_policy_response_default import RhubapipoliciesupdatePolicyResponseDefault
from ...types import Response


def _get_kwargs(
    policy_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapipoliciesupdatePolicyJsonBody,
) -> Dict[str, Any]:
    url = "{}/policies/{policy_id}".format(client.base_url, policy_id=policy_id)

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
) -> Optional[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubapipoliciesupdatePolicyResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubapipoliciesupdatePolicyResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]:
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
    json_body: RhubapipoliciesupdatePolicyJsonBody,
) -> Response[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]:
    """Update policy

    Args:
        policy_id (int):
        json_body (RhubapipoliciesupdatePolicyJsonBody):

    Returns:
        Response[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    policy_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapipoliciesupdatePolicyJsonBody,
) -> Optional[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]:
    """Update policy

    Args:
        policy_id (int):
        json_body (RhubapipoliciesupdatePolicyJsonBody):

    Returns:
        Response[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    policy_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapipoliciesupdatePolicyJsonBody,
) -> Response[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]:
    """Update policy

    Args:
        policy_id (int):
        json_body (RhubapipoliciesupdatePolicyJsonBody):

    Returns:
        Response[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(**kwargs)

    return _build_response(response=response)


async def asyncio(
    policy_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubapipoliciesupdatePolicyJsonBody,
) -> Optional[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]:
    """Update policy

    Args:
        policy_id (int):
        json_body (RhubapipoliciesupdatePolicyJsonBody):

    Returns:
        Response[Union[RhubapipoliciesupdatePolicyResponse200, RhubapipoliciesupdatePolicyResponseDefault]]
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
