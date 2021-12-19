import click

from rhub_cli.api.lab.rhubapilabclustercreate_cluster_hosts import sync_detailed as hosts_create
from rhub_cli.api.lab.rhubapilabclusterdelete_cluster_hosts import sync_detailed as hosts_remove
from rhub_cli.api.lab.rhubapilabclusterlist_cluster_hosts import sync_detailed as hosts_get_list
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def hosts():
    pass


@hosts.command()
@click.argument("cluster_id", type=int)
@pass_api
def get_list(
    api: APIRequest,
    cluster_id,
):
    """Get cluster hosts"""

    response = hosts_get_list(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@hosts.command()
@click.argument("cluster_id", type=int)
@pass_api
def create(
    api: APIRequest,
    cluster_id,
):
    """Create or update cluster hosts"""
    # TODO: json_body

    response = hosts_create(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@hosts.command()
@click.argument("cluster_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    cluster_id,
):
    """Delete cluster hosts"""

    response = hosts_remove(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
