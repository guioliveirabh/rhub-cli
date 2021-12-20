import click

from rhub_cli.api.auth.rhubapiauthuseradd_user_group import sync_detailed as groups_create
from rhub_cli.api.auth.rhubapiauthuserdelete_user_group import sync_detailed as groups_remove
from rhub_cli.api.auth.rhubapiauthuserlist_user_groups import sync_detailed as groups_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapiauthuseradd_user_group_json_body import RhubapiauthuseraddUserGroupJsonBody
from rhub_cli.models.rhubapiauthuserdelete_user_group_json_body import RhubapiauthuserdeleteUserGroupJsonBody


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
@click.option("--id", required=True, type=str)
@pass_api
def create(
    api: APIRequest,
    user_id,
    id,
):
    """Add user to group"""
    json_body = RhubapiauthuseraddUserGroupJsonBody(
        id=id,
    )

    response = groups_create(
        user_id=user_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@groups.command()
@click.argument("user_id", type=str)
@click.option("--id", required=True, type=str)
@pass_api
def remove(
    api: APIRequest,
    user_id,
    id,
):
    """Remove user from group"""
    json_body = RhubapiauthuserdeleteUserGroupJsonBody(
        id=id,
    )

    response = groups_remove(
        user_id=user_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
