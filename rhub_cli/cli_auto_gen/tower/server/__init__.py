import click

from rhub_cli.api.tower.rhubapitowercreate_server import sync_detailed as server_create
from rhub_cli.api.tower.rhubapitowerdelete_server import sync_detailed as server_remove
from rhub_cli.api.tower.rhubapitowerget_server import sync_detailed as server_get
from rhub_cli.api.tower.rhubapitowerlist_servers import sync_detailed as server_get_list
from rhub_cli.api.tower.rhubapitowerupdate_server import sync_detailed as server_update
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def server():
    pass


@server.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get list of Tower servers"""
    # TODO: query_parameters

    response = server_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create Tower server"""
    # TODO: json_body

    response = server_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.argument("server_id", type=int)
@pass_api
def get(
    api: APIRequest,
    server_id,
):
    """Get Tower server"""

    response = server_get(
        server_id=server_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.argument("server_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    server_id,
):
    """"""

    response = server_remove(
        server_id=server_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.argument("server_id", type=int)
@pass_api
def update(
    api: APIRequest,
    server_id,
):
    """Change Tower server"""
    # TODO: json_body

    response = server_update(
        server_id=server_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
