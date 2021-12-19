import click

from rhub_cli.api.auth.rhubapiauthgroupcreate_group import sync_detailed as group_create
from rhub_cli.api.auth.rhubapiauthgroupdelete_group import sync_detailed as group_remove
from rhub_cli.api.auth.rhubapiauthgroupget_group import sync_detailed as group_get
from rhub_cli.api.auth.rhubapiauthgrouplist_groups import sync_detailed as group_get_list
from rhub_cli.api.auth.rhubapiauthgroupupdate_group import sync_detailed as group_update
from rhub_cli.api_request import APIRequest, pass_api

from .roles import roles
from .users import users


@click.group()
def group():
    pass


@group.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get group list"""

    response = group_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@group.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create group"""
    # TODO: json_body

    response = group_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@group.command()
@click.argument("group_id", type=str)
@pass_api
def get(
    api: APIRequest,
    group_id,
):
    """Get group"""

    response = group_get(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@group.command()
@click.argument("group_id", type=str)
@pass_api
def remove(
    api: APIRequest,
    group_id,
):
    """Delete group"""

    response = group_remove(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@group.command()
@click.argument("group_id", type=str)
@pass_api
def update(
    api: APIRequest,
    group_id,
):
    """Update group"""
    # TODO: json_body

    response = group_update(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


group.add_command(roles)
group.add_command(users)
