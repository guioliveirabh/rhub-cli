import click

from rhub_cli.api.auth.rhubapiauthusercreate_user import sync_detailed as user_create
from rhub_cli.api.auth.rhubapiauthuserdelete_user import sync_detailed as user_remove
from rhub_cli.api.auth.rhubapiauthuserget_user import sync_detailed as user_get
from rhub_cli.api.auth.rhubapiauthuserlist_users import sync_detailed as user_get_list
from rhub_cli.api.auth.rhubapiauthuserupdate_user import sync_detailed as user_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapiauthusercreate_user_json_body import RhubapiauthusercreateUserJsonBody
from rhub_cli.models.rhubapiauthuserupdate_user_json_body import RhubapiauthuserupdateUserJsonBody

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
@click.option("--email", type=str)
@click.option("--username", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--first-name", type=str)
@click.option("--last-name", type=str)
@click.option("--password", type=str)
@pass_api
def create(
    api: APIRequest,
    email,
    username,
    enabled,
    first_name,
    last_name,
    password,
):
    """Create user"""

    json_body = RhubapiauthusercreateUserJsonBody(
        email=email,
        username=username,
        enabled=enabled,
        first_name=first_name,
        last_name=last_name,
        password=password,
    )

    response = user_create(
        json_body=json_body,
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
@click.option("--email", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--first-name", type=str)
@click.option("--last-name", type=str)
@click.option("--password", type=str)
@click.option("--username", type=str)
@pass_api
def update(
    api: APIRequest,
    user_id,
    email,
    enabled,
    first_name,
    last_name,
    password,
    username,
):
    """Update user"""

    json_body = RhubapiauthuserupdateUserJsonBody(
        email=email,
        enabled=enabled,
        first_name=first_name,
        last_name=last_name,
        password=password,
        username=username,
    )

    response = user_update(
        user_id=user_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


user.add_command(groups)
user.add_command(roles)
