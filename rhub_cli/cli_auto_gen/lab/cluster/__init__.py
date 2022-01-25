import click

from rhub_cli.api.lab.rhub_api_lab_cluster_create_cluster import sync_detailed as cluster_create
from rhub_cli.api.lab.rhub_api_lab_cluster_delete_cluster import sync_detailed as cluster_remove
from rhub_cli.api.lab.rhub_api_lab_cluster_get_cluster import sync_detailed as cluster_get
from rhub_cli.api.lab.rhub_api_lab_cluster_list_clusters import sync_detailed as cluster_get_list
from rhub_cli.api.lab.rhub_api_lab_cluster_update_cluster import sync_detailed as cluster_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_json_body import RhubApiLabClusterCreateClusterJsonBody
from rhub_cli.models.rhub_api_lab_cluster_update_cluster_json_body import RhubApiLabClusterUpdateClusterJsonBody

from .events import events
from .hosts import hosts
from .reboot import reboot


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
@click.option("--created", type=click.DateTime())
@click.option("--description", type=str)
@click.option("--group-id", type=str)
@click.option("--group-name", type=str)
@click.option("--hosts-fqdn", type=str)
@click.option("--hosts-ipaddr", type=str, multiple=True)
@click.option("--hosts-num-vcpus", type=int)
@click.option("--hosts-num-volumes", type=int)
@click.option("--hosts-ram-mb", type=int)
@click.option("--hosts-volumes-gb", type=int)
@click.option("--lifespan-expiration", type=click.DateTime())
@click.option("--name", type=str)
@click.option("--product-id", type=int)
@click.option("--product-name", type=str)
@click.option("--quota")
@click.option("--quota-usage")
@click.option("--region-id", type=int)
@click.option("--region-name", type=str)
@click.option("--reservation-expiration", type=click.DateTime())
@click.option("--shared", is_flag=True)
@click.option("--status")
@click.option("--user-id", type=str)
@click.option("--user-name", type=str)
@pass_api
def create(
    api: APIRequest,
    created,
    description,
    group_id,
    group_name,
    hosts_fqdn,
    hosts_ipaddr,
    hosts_num_vcpus,
    hosts_num_volumes,
    hosts_ram_mb,
    hosts_volumes_gb,
    lifespan_expiration,
    name,
    product_id,
    product_name,
    quota,
    quota_usage,
    region_id,
    region_name,
    reservation_expiration,
    shared,
    status,
    user_id,
    user_name,
):
    """Create cluster"""

    json_body = RhubApiLabClusterCreateClusterJsonBody(
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
        quota_usage=quota_usage,
        region_id=region_id,
        region_name=region_name,
        reservation_expiration=reservation_expiration,
        shared=shared,
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
@click.option("--created", type=click.DateTime())
@click.option("--description", type=str)
@click.option("--group-id", type=str)
@click.option("--group-name", type=str)
@click.option("--hosts-fqdn", type=str)
@click.option("--hosts-ipaddr", type=str, multiple=True)
@click.option("--hosts-num-vcpus", type=int)
@click.option("--hosts-num-volumes", type=int)
@click.option("--hosts-ram-mb", type=int)
@click.option("--hosts-volumes-gb", type=int)
@click.option("--lifespan-expiration", type=click.DateTime())
@click.option("--name", type=str)
@click.option("--product-id", type=int)
@click.option("--product-name", type=str)
@click.option("--quota")
@click.option("--quota-usage")
@click.option("--region-id", type=int)
@click.option("--region-name", type=str)
@click.option("--reservation-expiration", type=click.DateTime())
@click.option("--shared", is_flag=True)
@click.option("--status")
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
    hosts_fqdn,
    hosts_ipaddr,
    hosts_num_vcpus,
    hosts_num_volumes,
    hosts_ram_mb,
    hosts_volumes_gb,
    lifespan_expiration,
    name,
    product_id,
    product_name,
    quota,
    quota_usage,
    region_id,
    region_name,
    reservation_expiration,
    shared,
    status,
    user_id,
    user_name,
):
    """Update cluster"""

    json_body = RhubApiLabClusterUpdateClusterJsonBody(
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
        quota_usage=quota_usage,
        region_id=region_id,
        region_name=region_name,
        reservation_expiration=reservation_expiration,
        shared=shared,
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
cluster.add_command(reboot)
