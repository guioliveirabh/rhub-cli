from typing import Any, Dict, List, Union

import click

from rhub_cli.api.lab.rhubapilabclustercreate_cluster import sync_detailed as cluster_create
from rhub_cli.api.lab.rhubapilabclusterdelete_cluster import sync_detailed as cluster_remove
from rhub_cli.api.lab.rhubapilabclusterget_cluster import sync_detailed as cluster_get
from rhub_cli.api.lab.rhubapilabclusterlist_clusters import sync_detailed as cluster_get_list
from rhub_cli.api.lab.rhubapilabclusterupdate_cluster import sync_detailed as cluster_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapilabclustercreate_cluster_json_body import RhubapilabclustercreateClusterJsonBody
from rhub_cli.models.rhubapilabclusterupdate_cluster_json_body import RhubapilabclusterupdateClusterJsonBody

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
@click.option("--created", type=str)
@click.option("--description", type=str)
@click.option("--group-id", type=str)
@click.option("--group-name", type=str)
@click.option("--hosts", type=List[Dict[str, Any]])
@click.option("--lifespan-expiration", type=str)
@click.option("--name", type=str)
@click.option("--product-id", type=int)
@click.option("--product-name", type=str)
@click.option("--quota", type=Union[Any, Dict[str, Any]])
@click.option("--region-id", type=int)
@click.option("--region-name", type=str)
@click.option("--reservation-expiration", type=str)
@click.option("--status", type=str)
@click.option("--user-id", type=str)
@click.option("--user-name", type=str)
@pass_api
def create(
    api: APIRequest,
    created,
    description,
    group_id,
    group_name,
    hosts,
    lifespan_expiration,
    name,
    product_id,
    product_name,
    quota,
    region_id,
    region_name,
    reservation_expiration,
    status,
    user_id,
    user_name,
):
    """Create cluster"""
    json_body = RhubapilabclustercreateClusterJsonBody(
        created=created,
        description=description,
        group_id=group_id,
        group_name=group_name,
        hosts=hosts,
        lifespan_expiration=lifespan_expiration,
        name=name,
        product_id=product_id,
        product_name=product_name,
        quota=quota,
        region_id=region_id,
        region_name=region_name,
        reservation_expiration=reservation_expiration,
        status=status,
        user_id=user_id,
        user_name=user_name,
    )

    response = cluster_create(
        json_body=json_body,
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
@click.option("--created", type=str)
@click.option("--description", type=str)
@click.option("--group-id", type=str)
@click.option("--group-name", type=str)
@click.option("--hosts", type=List[Dict[str, Any]])
@click.option("--lifespan-expiration", type=str)
@click.option("--name", type=str)
@click.option("--product-id", type=int)
@click.option("--product-name", type=str)
@click.option("--quota", type=Union[Any, Dict[str, Any]])
@click.option("--region-id", type=int)
@click.option("--region-name", type=str)
@click.option("--reservation-expiration", type=str)
@click.option("--status", type=str)
@click.option("--user-id", type=str)
@click.option("--user-name", type=str)
@pass_api
def update(
    api: APIRequest,
    cluster_id,
    created,
    description,
    group_id,
    group_name,
    hosts,
    lifespan_expiration,
    name,
    product_id,
    product_name,
    quota,
    region_id,
    region_name,
    reservation_expiration,
    status,
    user_id,
    user_name,
):
    """Update cluster"""
    json_body = RhubapilabclusterupdateClusterJsonBody(
        created=created,
        description=description,
        group_id=group_id,
        group_name=group_name,
        hosts=hosts,
        lifespan_expiration=lifespan_expiration,
        name=name,
        product_id=product_id,
        product_name=product_name,
        quota=quota,
        region_id=region_id,
        region_name=region_name,
        reservation_expiration=reservation_expiration,
        status=status,
        user_id=user_id,
        user_name=user_name,
    )

    response = cluster_update(
        cluster_id=cluster_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


cluster.add_command(events)
cluster.add_command(hosts)
