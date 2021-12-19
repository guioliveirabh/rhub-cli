import click

from rhub_cli.api.lab.rhubapilabclustercreate_cluster import sync_detailed as cluster_create
from rhub_cli.api.lab.rhubapilabclusterdelete_cluster import sync_detailed as cluster_remove
from rhub_cli.api.lab.rhubapilabclusterget_cluster import sync_detailed as cluster_get
from rhub_cli.api.lab.rhubapilabclusterlist_clusters import sync_detailed as cluster_get_list
from rhub_cli.api.lab.rhubapilabclusterupdate_cluster import sync_detailed as cluster_update
from rhub_cli.api_request import APIRequest, pass_api

from .events import events
from .hosts import hosts


@click.group()
def cluster():
    pass


@cluster.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get cluster list"""
    # TODO: query_parameters

    response = cluster_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cluster.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create cluster"""
    # TODO: json_body

    response = cluster_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cluster.command()
@click.argument("cluster_id", type=int)
@pass_api
def get(
    api: APIRequest,
    cluster_id,
):
    """Get cluster"""

    response = cluster_get(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cluster.command()
@click.argument("cluster_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    cluster_id,
):
    """Delete cluster"""

    response = cluster_remove(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cluster.command()
@click.argument("cluster_id", type=int)
@pass_api
def update(
    api: APIRequest,
    cluster_id,
):
    """Update cluster"""
    # TODO: json_body

    response = cluster_update(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


cluster.add_command(events)
cluster.add_command(hosts)
