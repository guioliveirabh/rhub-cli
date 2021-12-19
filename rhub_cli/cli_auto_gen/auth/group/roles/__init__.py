import click

from rhub_cli.api.auth.rhubapiauthgroupadd_group_role import sync_detailed as roles_create
from rhub_cli.api.auth.rhubapiauthgroupdelete_group_role import sync_detailed as roles_remove
from rhub_cli.api.auth.rhubapiauthgrouplist_group_roles import sync_detailed as roles_get_list
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def roles():
    pass


@roles.command()
@click.argument("group_id", type=str)
@pass_api
def get_list(
    api: APIRequest,
    group_id,
):
    """Get group roles"""

    response = roles_get_list(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@roles.command()
@click.argument("group_id", type=str)
@pass_api
def create(
    api: APIRequest,
    group_id,
):
    """Add group to role"""
    # TODO: json_body

    response = roles_create(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@roles.command()
@click.argument("group_id", type=str)
@pass_api
def remove(
    api: APIRequest,
    group_id,
):
    """Remove group from role"""
    # TODO: json_body

    response = roles_remove(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
