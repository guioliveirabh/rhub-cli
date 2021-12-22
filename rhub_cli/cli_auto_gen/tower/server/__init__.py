import click

from rhub_cli.api.tower.rhubapitowercreate_server import sync_detailed as server_create
from rhub_cli.api.tower.rhubapitowerdelete_server import sync_detailed as server_remove
from rhub_cli.api.tower.rhubapitowerget_server import sync_detailed as server_get
from rhub_cli.api.tower.rhubapitowerlist_servers import sync_detailed as server_get_list
from rhub_cli.api.tower.rhubapitowerupdate_server import sync_detailed as server_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapitowercreate_server_json_body import RhubapitowercreateServerJsonBody
from rhub_cli.models.rhubapitowerupdate_server_json_body import RhubapitowerupdateServerJsonBody


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
@click.option("--credentials", type=str)
@click.option("--name", type=str)
@click.option("--url", type=str)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--verify-ssl", is_flag=True)
@pass_api
def create(
    api: APIRequest,
    credentials,
    name,
    url,
    description,
    enabled,
    verify_ssl,
):
    """Create Tower server"""

    json_body = RhubapitowercreateServerJsonBody(
        credentials=credentials,
        name=name,
        url=url,
        description=description,
        enabled=enabled,
        verify_ssl=verify_ssl,
    )

    response = server_create(
        json_body=json_body,
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
@click.option("--credentials", type=str)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--name", type=str)
@click.option("--url", type=str)
@click.option("--verify-ssl", is_flag=True)
@pass_api
def update(
    api: APIRequest,
    server_id,
    credentials,
    description,
    enabled,
    name,
    url,
    verify_ssl,
):
    """Change Tower server"""

    json_body = RhubapitowerupdateServerJsonBody(
        credentials=credentials,
        description=description,
        enabled=enabled,
        name=name,
        url=url,
        verify_ssl=verify_ssl,
    )

    response = server_update(
        server_id=server_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
