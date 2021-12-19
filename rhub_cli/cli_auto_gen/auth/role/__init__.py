import click

from rhub_cli.api.auth.rhubapiauthrolecreate_role import sync_detailed as role_create
from rhub_cli.api.auth.rhubapiauthroledelete_role import sync_detailed as role_remove
from rhub_cli.api.auth.rhubapiauthroleget_role import sync_detailed as role_get
from rhub_cli.api.auth.rhubapiauthrolelist_roles import sync_detailed as role_get_list
from rhub_cli.api.auth.rhubapiauthroleupdate_role import sync_detailed as role_update
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def role():
    pass


@role.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get role list"""

    response = role_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@role.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create role"""
    # TODO: json_body

    response = role_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@role.command()
@click.argument("role_id", type=str)
@pass_api
def get(
    api: APIRequest,
    role_id,
):
    """Get role"""

    response = role_get(
        role_id=role_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@role.command()
@click.argument("role_id", type=str)
@pass_api
def remove(
    api: APIRequest,
    role_id,
):
    """Delete role"""

    response = role_remove(
        role_id=role_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@role.command()
@click.argument("role_id", type=str)
@pass_api
def update(
    api: APIRequest,
    role_id,
):
    """Update role"""
    # TODO: json_body

    response = role_update(
        role_id=role_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
