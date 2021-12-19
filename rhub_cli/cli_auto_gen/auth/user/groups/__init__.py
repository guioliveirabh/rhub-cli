import click

from rhub_cli.api.auth.rhubapiauthuseradd_user_group import sync_detailed as groups_create
from rhub_cli.api.auth.rhubapiauthuserdelete_user_group import sync_detailed as groups_remove
from rhub_cli.api.auth.rhubapiauthuserlist_user_groups import sync_detailed as groups_get_list
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def groups():
    pass


@groups.command()
@click.argument("user_id", type=str)
@pass_api
def get_list(
    api: APIRequest,
    user_id,
):
    """Get user groups"""

    response = groups_get_list(
        user_id=user_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@groups.command()
@click.argument("user_id", type=str)
@pass_api
def create(
    api: APIRequest,
    user_id,
):
    """Add user to group"""
    # TODO: json_body

    response = groups_create(
        user_id=user_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@groups.command()
@click.argument("user_id", type=str)
@pass_api
def remove(
    api: APIRequest,
    user_id,
):
    """Remove user from group"""
    # TODO: json_body

    response = groups_remove(
        user_id=user_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
