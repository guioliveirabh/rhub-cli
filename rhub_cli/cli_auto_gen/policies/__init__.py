import click

from rhub_cli.api.policy.rhub_api_policies_create_policy import sync_detailed as policies_create
from rhub_cli.api.policy.rhub_api_policies_delete_policy import sync_detailed as policies_remove
from rhub_cli.api.policy.rhub_api_policies_get_policy import sync_detailed as policies_get
from rhub_cli.api.policy.rhub_api_policies_list_policies import sync_detailed as policies_get_list
from rhub_cli.api.policy.rhub_api_policies_update_policy import sync_detailed as policies_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models import *
from rhub_cli.models.rhub_api_policies_create_policy_json_body import RhubApiPoliciesCreatePolicyJsonBody
from rhub_cli.models.rhub_api_policies_update_policy_json_body import RhubApiPoliciesUpdatePolicyJsonBody


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
@click.option("--department", type=str)
@click.option("--name", type=str)
@click.option("--constraint-cost", type=float)
@click.option("--constraint-density", type=str)
@click.option("--constraint-location", type=str)
@click.option("--constraint-sched-avail", type=click.DateTime(), multiple=True)
@click.option("--constraint-serv-avail", type=float)
@click.option("--constraint-tag", type=str, multiple=True)
@pass_api
def create(
    api: APIRequest,
    department,
    name,
    constraint_cost,
    constraint_density,
    constraint_location,
    constraint_sched_avail,
    constraint_serv_avail,
    constraint_tag,
):
    """Create policy"""

    constraint = RhubApiPoliciesCreatePolicyJsonBodyConstraint(
        cost=constraint_cost,
        density=constraint_density,
        location=constraint_location,
        sched_avail=constraint_sched_avail,
        serv_avail=constraint_serv_avail,
        tag=constraint_tag,
    )

    json_body = RhubApiPoliciesCreatePolicyJsonBody(
        department=department,
        name=name,
        constraint=constraint,
    )

    response = policies_create(
        json_body=json_body,
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
@click.option("--constraint-cost", type=float)
@click.option("--constraint-density", type=str)
@click.option("--constraint-location", type=str)
@click.option("--constraint-sched-avail", type=click.DateTime(), multiple=True)
@click.option("--constraint-serv-avail", type=float)
@click.option("--constraint-tag", type=str, multiple=True)
@click.option("--department", type=str)
@click.option("--name", type=str)
@pass_api
def update(
    api: APIRequest,
    policy_id,
    constraint_cost,
    constraint_density,
    constraint_location,
    constraint_sched_avail,
    constraint_serv_avail,
    constraint_tag,
    department,
    name,
):
    """Update policy"""

    constraint = RhubApiPoliciesUpdatePolicyJsonBodyConstraint(
        cost=constraint_cost,
        density=constraint_density,
        location=constraint_location,
        sched_avail=constraint_sched_avail,
        serv_avail=constraint_serv_avail,
        tag=constraint_tag,
    )

    json_body = RhubApiPoliciesUpdatePolicyJsonBody(
        constraint=constraint,
        department=department,
        name=name,
    )

    response = policies_update(
        policy_id=policy_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
