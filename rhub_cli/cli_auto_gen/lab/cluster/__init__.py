import json

import click

from rhub_cli.api.lab.rhub_api_lab_cluster_create_cluster import sync_detailed as cluster_create
from rhub_cli.api.lab.rhub_api_lab_cluster_delete_cluster import sync_detailed as cluster_remove
from rhub_cli.api.lab.rhub_api_lab_cluster_get_cluster import sync_detailed as cluster_get
from rhub_cli.api.lab.rhub_api_lab_cluster_list_clusters import sync_detailed as cluster_get_list
from rhub_cli.api.lab.rhub_api_lab_cluster_update_cluster import sync_detailed as cluster_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_json_body import RhubApiLabClusterCreateClusterJsonBody
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_json_body_hosts_item import (
    RhubApiLabClusterCreateClusterJsonBodyHostsItem,
)
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_json_body_product_params import (
    RhubApiLabClusterCreateClusterJsonBodyProductParams,
)
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_json_body_status import (
    RhubApiLabClusterCreateClusterJsonBodyStatus,
)
from rhub_cli.models.rhub_api_lab_cluster_list_clusters_filter import RhubApiLabClusterListClustersFilter
from rhub_cli.models.rhub_api_lab_cluster_list_clusters_sort import RhubApiLabClusterListClustersSort
from rhub_cli.models.rhub_api_lab_cluster_update_cluster_json_body import RhubApiLabClusterUpdateClusterJsonBody
from rhub_cli.models.rhub_api_lab_cluster_update_cluster_json_body_hosts_item import (
    RhubApiLabClusterUpdateClusterJsonBodyHostsItem,
)
from rhub_cli.models.rhub_api_lab_cluster_update_cluster_json_body_product_params import (
    RhubApiLabClusterUpdateClusterJsonBodyProductParams,
)
from rhub_cli.models.rhub_api_lab_cluster_update_cluster_json_body_status import (
    RhubApiLabClusterUpdateClusterJsonBodyStatus,
)
from rhub_cli.types import UNSET

from .events import events
from .hosts import hosts
from .reboot import reboot


@click.group()
def cluster():
    pass


@cluster.command()
@click.option(
    "--sort",
    type=click.Choice(
        [
            "name",
            "-name",
            "reservation_expiration",
            "-reservation_expiration",
            "lifespan_expiration",
            "-lifespan_expiration",
        ]
    ),
)
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-group-id", type=str, help="ID of the group or ``null``.")
@click.option(
    "--filter-name",
    type=str,
    help="Name of a cluster. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@click.option("--filter-region-id", type=int, help="ID of the region.")
@click.option("--filter-shared", is_flag=True, help="Filter shared clusters")
@click.option("--filter-user-id", type=str, help="ID of the user.")
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_group_id,
    filter_name,
    filter_region_id,
    filter_shared,
    filter_user_id,
):
    """Get cluster list"""

    sort = RhubApiLabClusterListClustersSort(sort)

    filter_ = RhubApiLabClusterListClustersFilter(
        group_id=filter_group_id,
        name=filter_name,
        region_id=filter_region_id,
        shared=filter_shared,
        user_id=filter_user_id,
    )

    response = cluster_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cluster.command()
@click.option("--name", required=True, type=str)
@click.option("--product-id", required=True, type=int)
@click.option("--product-params", required=True)
@click.option("--region-id", required=True, type=int)
@click.option("--created", type=click.DateTime())
@click.option("--description", type=str)
@click.option("--group-id", type=str)
@click.option("--group-name", type=str)
@click.option("--lifespan-expiration", type=click.DateTime(), help="Hard-limit expiration.")
@click.option("--product-name", type=str)
@click.option("--quota")
@click.option("--quota-usage")
@click.option("--region-name", type=str)
@click.option("--reservation-expiration", type=click.DateTime(), help="Soft-limit expiration.")
@click.option("--shared", is_flag=True)
@click.option(
    "--status",
    type=click.Choice(
        [
            "Active",
            "Deleted",
            "Deleting",
            "Deletion Failed",
            "Deletion Queued",
            "Installation Failed",
            "Installation Queued",
            "Installing",
            "Post-Deleting",
            "Post-Deletion Failed",
            "Post-Deletion Queued",
            "Post-Installation Failed",
            "Post-Installation Queued",
            "Post-Installing",
            "Post-Provisioning",
            "Post-Provisioning Failed",
            "Post-Provisioning Queued",
            "Pre-Deleting",
            "Pre-Deletion Failed",
            "Pre-Deletion Queued",
            "Pre-Installation Failed",
            "Pre-Installation Queued",
            "Pre-Installing",
            "Pre-Provisioning",
            "Pre-Provisioning Failed",
            "Pre-Provisioning Queued",
            "Provisioning",
            "Provisioning Failed",
            "Provisioning Queued",
            "Queued",
        ]
    ),
)
@click.option("--user-id", type=str)
@click.option("--user-name", type=str)
@click.option("--hosts-item-fqdn", type=str)
@click.option("--hosts-item-ipaddr-item", type=str)
@click.option("--hosts-item-num-vcpus", type=int)
@click.option("--hosts-item-num-volumes", type=int)
@click.option("--hosts-item-ram-mb", type=int)
@click.option("--hosts-item-volumes-gb", type=int)
@click.option("--hosts-item-cluster-id", type=int)
@click.option("--hosts-item-id", type=int)
@pass_api
def create(
    api: APIRequest,
    name,
    product_id,
    product_params,
    region_id,
    created,
    description,
    group_id,
    group_name,
    lifespan_expiration,
    product_name,
    quota,
    quota_usage,
    region_name,
    reservation_expiration,
    shared,
    status,
    user_id,
    user_name,
    hosts_item_fqdn,
    hosts_item_ipaddr_item,
    hosts_item_num_vcpus,
    hosts_item_num_volumes,
    hosts_item_ram_mb,
    hosts_item_volumes_gb,
    hosts_item_cluster_id,
    hosts_item_id,
):
    """Create cluster"""

    hosts_item_ipaddr = []
    if hosts_item_ipaddr_item is not None:
        hosts_item_ipaddr.append(hosts_item_ipaddr_item)

    status = RhubApiLabClusterCreateClusterJsonBodyStatus(status)

    hosts_item = RhubApiLabClusterCreateClusterJsonBodyHostsItem(
        fqdn=hosts_item_fqdn,
        ipaddr=hosts_item_ipaddr,
        num_vcpus=hosts_item_num_vcpus,
        num_volumes=hosts_item_num_volumes,
        ram_mb=hosts_item_ram_mb,
        volumes_gb=hosts_item_volumes_gb,
        cluster_id=hosts_item_cluster_id,
        id=hosts_item_id,
    )

    hosts = []
    if hosts_item is not None:
        hosts.append(hosts_item)

    if product_params is None:
        product_params = UNSET
    else:
        _tmp = RhubApiLabClusterCreateClusterJsonBodyProductParams()
        _tmp.additional_properties = json.loads(product_params)  # TODO: check if dict
        product_params = _tmp

    json_body = RhubApiLabClusterCreateClusterJsonBody(
        name=name,
        product_id=product_id,
        product_params=product_params,
        region_id=region_id,
        created=created,
        description=description,
        group_id=group_id,
        group_name=group_name,
        hosts=hosts,
        lifespan_expiration=lifespan_expiration,
        product_name=product_name,
        quota=quota,
        quota_usage=quota_usage,
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
@click.option("--lifespan-expiration", type=click.DateTime(), help="Hard-limit expiration.")
@click.option("--name", type=str)
@click.option("--product-id", type=int)
@click.option("--product-name", type=str)
@click.option("--product-params")
@click.option("--quota")
@click.option("--quota-usage")
@click.option("--region-id", type=int)
@click.option("--region-name", type=str)
@click.option("--reservation-expiration", type=click.DateTime(), help="Soft-limit expiration.")
@click.option("--shared", is_flag=True)
@click.option(
    "--status",
    type=click.Choice(
        [
            "Active",
            "Deleted",
            "Deleting",
            "Deletion Failed",
            "Deletion Queued",
            "Installation Failed",
            "Installation Queued",
            "Installing",
            "Post-Deleting",
            "Post-Deletion Failed",
            "Post-Deletion Queued",
            "Post-Installation Failed",
            "Post-Installation Queued",
            "Post-Installing",
            "Post-Provisioning",
            "Post-Provisioning Failed",
            "Post-Provisioning Queued",
            "Pre-Deleting",
            "Pre-Deletion Failed",
            "Pre-Deletion Queued",
            "Pre-Installation Failed",
            "Pre-Installation Queued",
            "Pre-Installing",
            "Pre-Provisioning",
            "Pre-Provisioning Failed",
            "Pre-Provisioning Queued",
            "Provisioning",
            "Provisioning Failed",
            "Provisioning Queued",
            "Queued",
        ]
    ),
)
@click.option("--user-id", type=str)
@click.option("--user-name", type=str)
@click.option("--hosts-item-fqdn", type=str)
@click.option("--hosts-item-ipaddr-item", type=str)
@click.option("--hosts-item-num-vcpus", type=int)
@click.option("--hosts-item-num-volumes", type=int)
@click.option("--hosts-item-ram-mb", type=int)
@click.option("--hosts-item-volumes-gb", type=int)
@click.option("--hosts-item-cluster-id", type=int)
@click.option("--hosts-item-id", type=int)
@pass_api
def update(
    api: APIRequest,
    cluster_id,
    created,
    description,
    group_id,
    group_name,
    lifespan_expiration,
    name,
    product_id,
    product_name,
    product_params,
    quota,
    quota_usage,
    region_id,
    region_name,
    reservation_expiration,
    shared,
    status,
    user_id,
    user_name,
    hosts_item_fqdn,
    hosts_item_ipaddr_item,
    hosts_item_num_vcpus,
    hosts_item_num_volumes,
    hosts_item_ram_mb,
    hosts_item_volumes_gb,
    hosts_item_cluster_id,
    hosts_item_id,
):
    """Update cluster"""

    hosts_item_ipaddr = []
    if hosts_item_ipaddr_item is not None:
        hosts_item_ipaddr.append(hosts_item_ipaddr_item)

    status = RhubApiLabClusterUpdateClusterJsonBodyStatus(status)

    if product_params is None:
        product_params = UNSET
    else:
        _tmp = RhubApiLabClusterUpdateClusterJsonBodyProductParams()
        _tmp.additional_properties = json.loads(product_params)  # TODO: check if dict
        product_params = _tmp

    hosts_item = RhubApiLabClusterUpdateClusterJsonBodyHostsItem(
        fqdn=hosts_item_fqdn,
        ipaddr=hosts_item_ipaddr,
        num_vcpus=hosts_item_num_vcpus,
        num_volumes=hosts_item_num_volumes,
        ram_mb=hosts_item_ram_mb,
        volumes_gb=hosts_item_volumes_gb,
        cluster_id=hosts_item_cluster_id,
        id=hosts_item_id,
    )

    hosts = []
    if hosts_item is not None:
        hosts.append(hosts_item)

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
        product_params=product_params,
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
