import click

from rhub_cli.api.policy.rhubapipoliciescreate_policy import sync_detailed as policies_create
from rhub_cli.api.policy.rhubapipoliciesdelete_policy import sync_detailed as policies_remove
from rhub_cli.api.policy.rhubapipoliciesget_policy import sync_detailed as policies_get
from rhub_cli.api.policy.rhubapipolicieslist_policies import sync_detailed as policies_get_list
from rhub_cli.api.policy.rhubapipoliciesupdate_policy import sync_detailed as policies_update
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def policies():
    pass


@policies.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get policy list"""
    # TODO: query_parameters

    response = policies_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@policies.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create policy"""
    # TODO: json_body

    response = policies_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@policies.command()
@click.argument("policy_id", type=int)
@pass_api
def get(
    api: APIRequest,
    policy_id,
):
    """Get policy"""

    response = policies_get(
        policy_id=policy_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@policies.command()
@click.argument("policy_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    policy_id,
):
    """Delete policy"""

    response = policies_remove(
        policy_id=policy_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@policies.command()
@click.argument("policy_id", type=int)
@pass_api
def update(
    api: APIRequest,
    policy_id,
):
    """Update policy"""
    # TODO: json_body

    response = policies_update(
        policy_id=policy_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
