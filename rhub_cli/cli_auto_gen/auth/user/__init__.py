import click

from rhub_cli.api.auth.rhubapiauthusercreate_user import sync_detailed as user_create
from rhub_cli.api.auth.rhubapiauthuserdelete_user import sync_detailed as user_remove
from rhub_cli.api.auth.rhubapiauthuserget_user import sync_detailed as user_get
from rhub_cli.api.auth.rhubapiauthuserlist_users import sync_detailed as user_get_list
from rhub_cli.api.auth.rhubapiauthuserupdate_user import sync_detailed as user_update
from rhub_cli.api_request import APIRequest, pass_api

from .groups import groups
from .roles import roles


@click.group()
def user():
    pass


@user.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get user list"""
    # TODO: query_parameters

    response = user_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@user.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create user"""
    # TODO: json_body

    response = user_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@user.command()
@click.argument("user_id", type=str)
@pass_api
def get(
    api: APIRequest,
    user_id,
):
    """Get user"""

    response = user_get(
        user_id=user_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@user.command()
@click.argument("user_id", type=str)
@pass_api
def remove(
    api: APIRequest,
    user_id,
):
    """Delete user"""

    response = user_remove(
        user_id=user_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@user.command()
@click.argument("user_id", type=str)
@pass_api
def update(
    api: APIRequest,
    user_id,
):
    """Update user"""
    # TODO: json_body

    response = user_update(
        user_id=user_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


user.add_command(groups)
user.add_command(roles)
