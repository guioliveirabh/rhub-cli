import click

from rhub_cli.api.auth.rhub_api_auth_role_create_role import sync_detailed as role_create
from rhub_cli.api.auth.rhub_api_auth_role_delete_role import sync_detailed as role_remove
from rhub_cli.api.auth.rhub_api_auth_role_get_role import sync_detailed as role_get
from rhub_cli.api.auth.rhub_api_auth_role_list_roles import sync_detailed as role_get_list
from rhub_cli.api.auth.rhub_api_auth_role_update_role import sync_detailed as role_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_auth_role_create_role_json_body import RhubApiAuthRoleCreateRoleJsonBody
from rhub_cli.models.rhub_api_auth_role_update_role_json_body import RhubApiAuthRoleUpdateRoleJsonBody


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
@click.option("--name", required=True, type=str)
@pass_api
def create(
    api: APIRequest,
    name,
):
    """Create role"""

    json_body = RhubApiAuthRoleCreateRoleJsonBody(
        name=name,
    )

    response = role_create(
        json_body=json_body,
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
@click.option("--name", type=str)
@pass_api
def update(
    api: APIRequest,
    role_id,
    name,
):
    """Update role"""

    json_body = RhubApiAuthRoleUpdateRoleJsonBody(
        name=name,
    )

    response = role_update(
        role_id=role_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
