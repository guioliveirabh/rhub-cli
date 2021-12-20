import click

from rhub_cli.api.auth.rhubapiauthuseradd_user_role import sync_detailed as roles_create
from rhub_cli.api.auth.rhubapiauthuserdelete_user_role import sync_detailed as roles_remove
from rhub_cli.api.auth.rhubapiauthuserlist_user_roles import sync_detailed as roles_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapiauthuseradd_user_role_json_body import RhubapiauthuseraddUserRoleJsonBody
from rhub_cli.models.rhubapiauthuserdelete_user_role_json_body import RhubapiauthuserdeleteUserRoleJsonBody


@click.group()
def roles():
    pass


@roles.command()
@click.argument("user_id", type=str)
@pass_api
def get_list(
    api: APIRequest,
    user_id,
):
    """Get user roles"""

    response = roles_get_list(
        user_id=user_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@roles.command()
@click.argument("user_id", type=str)
@click.option("--id", required=True, type=str)
@pass_api
def create(
    api: APIRequest,
    user_id,
    id,
):
    """Add user to role"""
    json_body = RhubapiauthuseraddUserRoleJsonBody(
        id=id,
    )

    response = roles_create(
        user_id=user_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@roles.command()
@click.argument("user_id", type=str)
@click.option("--id", required=True, type=str)
@pass_api
def remove(
    api: APIRequest,
    user_id,
    id,
):
    """Remove user from role"""
    json_body = RhubapiauthuserdeleteUserRoleJsonBody(
        id=id,
    )

    response = roles_remove(
        user_id=user_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
