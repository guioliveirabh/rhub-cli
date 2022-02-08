import click

from rhub_cli.api.tower.rhub_api_tower_create_server import sync_detailed as server_create
from rhub_cli.api.tower.rhub_api_tower_delete_server import sync_detailed as server_remove
from rhub_cli.api.tower.rhub_api_tower_get_server import sync_detailed as server_get
from rhub_cli.api.tower.rhub_api_tower_list_servers import sync_detailed as server_get_list
from rhub_cli.api.tower.rhub_api_tower_update_server import sync_detailed as server_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_tower_create_server_json_body import RhubApiTowerCreateServerJsonBody
from rhub_cli.models.rhub_api_tower_list_servers_filter import RhubApiTowerListServersFilter
from rhub_cli.models.rhub_api_tower_list_servers_sort import RhubApiTowerListServersSort
from rhub_cli.models.rhub_api_tower_update_server_json_body import RhubApiTowerUpdateServerJsonBody


@click.group()
def server():
    pass


@server.command()
@click.option("--filter-enabled", is_flag=True)
@click.option("--filter-name", type=str)
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@pass_api
def get_list(
    api: APIRequest,
    filter_enabled,
    filter_name,
    sort,
    page,
    limit,
):
    """Get list of Tower servers"""

    sort = RhubApiTowerListServersSort(sort)

    filter_ = RhubApiTowerListServersFilter(
        enabled=filter_enabled,
        name=filter_name,
    )

    response = server_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.option("--credentials", required=True, type=str)
@click.option("--name", required=True, type=str)
@click.option("--url", required=True, type=str)
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

    json_body = RhubApiTowerCreateServerJsonBody(
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

    json_body = RhubApiTowerUpdateServerJsonBody(
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
