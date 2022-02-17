import click

from rhub_cli.api.lab.rhub_api_lab_region_create_region import sync_detailed as region_create
from rhub_cli.api.lab.rhub_api_lab_region_delete_region import sync_detailed as region_remove
from rhub_cli.api.lab.rhub_api_lab_region_get_region import sync_detailed as region_get
from rhub_cli.api.lab.rhub_api_lab_region_list_regions import sync_detailed as region_get_list
from rhub_cli.api.lab.rhub_api_lab_region_update_region import sync_detailed as region_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_region_create_region_json_body import RhubApiLabRegionCreateRegionJsonBody
from rhub_cli.models.rhub_api_lab_region_create_region_json_body_total_quota import (
    RhubApiLabRegionCreateRegionJsonBodyTotalQuota,
)
from rhub_cli.models.rhub_api_lab_region_create_region_json_body_user_quota import (
    RhubApiLabRegionCreateRegionJsonBodyUserQuota,
)
from rhub_cli.models.rhub_api_lab_region_list_regions_filter import RhubApiLabRegionListRegionsFilter
from rhub_cli.models.rhub_api_lab_region_list_regions_sort import RhubApiLabRegionListRegionsSort
from rhub_cli.models.rhub_api_lab_region_update_region_json_body import RhubApiLabRegionUpdateRegionJsonBody
from rhub_cli.models.rhub_api_lab_region_update_region_json_body_dns_server import (
    RhubApiLabRegionUpdateRegionJsonBodyDnsServer,
)
from rhub_cli.models.rhub_api_lab_region_update_region_json_body_openstack import (
    RhubApiLabRegionUpdateRegionJsonBodyOpenstack,
)
from rhub_cli.models.rhub_api_lab_region_update_region_json_body_satellite import (
    RhubApiLabRegionUpdateRegionJsonBodySatellite,
)
from rhub_cli.models.rhub_api_lab_region_update_region_json_body_total_quota import (
    RhubApiLabRegionUpdateRegionJsonBodyTotalQuota,
)
from rhub_cli.models.rhub_api_lab_region_update_region_json_body_user_quota import (
    RhubApiLabRegionUpdateRegionJsonBodyUserQuota,
)

from .products import products
from .usage import usage


@click.group()
def region():
    pass


@region.command()
@click.option(
    "--sort",
    type=click.Choice(
        ["name", "-name", "location", "-location", "reservation_expiration_max", "-reservation_expiration_max"]
    ),
)
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-enabled", is_flag=True)
@click.option("--filter-location", type=str)
@click.option("--filter-name", type=str)
@click.option("--filter-reservations-enabled", is_flag=True)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_enabled,
    filter_location,
    filter_name,
    filter_reservations_enabled,
):
    """Get region list"""

    sort = RhubApiLabRegionListRegionsSort(sort)

    filter_ = RhubApiLabRegionListRegionsFilter(
        enabled=filter_enabled,
        location=filter_location,
        name=filter_name,
        reservations_enabled=filter_reservations_enabled,
    )

    response = region_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@region.command()
@click.option("--dns-server", required=True)
@click.option("--download-server", required=True, type=str)
@click.option("--name", required=True, type=str)
@click.option("--openstack", required=True)
@click.option("--satellite", required=True)
@click.option("--tower-id", required=True, type=int)
@click.option("--vault-server", required=True, type=str)
@click.option("--banner", type=str)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--lifespan-length", type=int)
@click.option("--location", type=str)
@click.option("--owner-group", type=str)
@click.option("--reservation-expiration-max", type=int)
@click.option("--reservations-enabled", is_flag=True)
@click.option("--users-group", type=str)
@click.option("--total-quota-num-vcpus", type=int)
@click.option("--total-quota-num-volumes", type=int)
@click.option("--total-quota-ram-mb", type=int)
@click.option("--total-quota-volumes-gb", type=int)
@click.option("--user-quota-num-vcpus", type=int)
@click.option("--user-quota-num-volumes", type=int)
@click.option("--user-quota-ram-mb", type=int)
@click.option("--user-quota-volumes-gb", type=int)
@pass_api
def create(
    api: APIRequest,
    dns_server,
    download_server,
    name,
    openstack,
    satellite,
    tower_id,
    vault_server,
    banner,
    description,
    enabled,
    lifespan_length,
    location,
    owner_group,
    reservation_expiration_max,
    reservations_enabled,
    users_group,
    total_quota_num_vcpus,
    total_quota_num_volumes,
    total_quota_ram_mb,
    total_quota_volumes_gb,
    user_quota_num_vcpus,
    user_quota_num_volumes,
    user_quota_ram_mb,
    user_quota_volumes_gb,
):
    """Create region"""

    user_quota = RhubApiLabRegionCreateRegionJsonBodyUserQuota(
        num_vcpus=user_quota_num_vcpus,
        num_volumes=user_quota_num_volumes,
        ram_mb=user_quota_ram_mb,
        volumes_gb=user_quota_volumes_gb,
    )

    total_quota = RhubApiLabRegionCreateRegionJsonBodyTotalQuota(
        num_vcpus=total_quota_num_vcpus,
        num_volumes=total_quota_num_volumes,
        ram_mb=total_quota_ram_mb,
        volumes_gb=total_quota_volumes_gb,
    )

    json_body = RhubApiLabRegionCreateRegionJsonBody(
        dns_server=dns_server,
        download_server=download_server,
        name=name,
        openstack=openstack,
        satellite=satellite,
        tower_id=tower_id,
        vault_server=vault_server,
        banner=banner,
        description=description,
        enabled=enabled,
        lifespan_length=lifespan_length,
        location=location,
        owner_group=owner_group,
        reservation_expiration_max=reservation_expiration_max,
        reservations_enabled=reservations_enabled,
        total_quota=total_quota,
        user_quota=user_quota,
        users_group=users_group,
    )

    response = region_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@region.command()
@click.argument("region_id", type=int)
@pass_api
def get(
    api: APIRequest,
    region_id,
):
    """Get region"""

    response = region_get(
        region_id=region_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@region.command()
@click.argument("region_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    region_id,
):
    """Delete region"""

    response = region_remove(
        region_id=region_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@region.command()
@click.argument("region_id", type=int)
@click.option("--banner", type=str)
@click.option("--description", type=str)
@click.option("--download-server", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--lifespan-length", type=int)
@click.option("--location", type=str)
@click.option("--name", type=str)
@click.option("--owner-group", type=str)
@click.option("--reservation-expiration-max", type=int)
@click.option("--reservations-enabled", is_flag=True)
@click.option("--tower-id", type=int)
@click.option("--users-group", type=str)
@click.option("--vault-server", type=str)
@click.option("--dns-server-hostname", type=str)
@click.option("--dns-server-key")
@click.option("--dns-server-zone", type=str)
@click.option("--openstack-credentials")
@click.option("--openstack-domain-id", type=str)
@click.option("--openstack-domain-name", type=str)
@click.option("--openstack-keyname", type=str)
@click.option("--openstack-networks-item", type=str)
@click.option("--openstack-project", type=str)
@click.option("--openstack-url", type=str)
@click.option("--satellite-credentials")
@click.option("--satellite-hostname", type=str)
@click.option("--satellite-insecure", is_flag=True)
@click.option("--total-quota-num-vcpus", type=int)
@click.option("--total-quota-num-volumes", type=int)
@click.option("--total-quota-ram-mb", type=int)
@click.option("--total-quota-volumes-gb", type=int)
@click.option("--user-quota-num-vcpus", type=int)
@click.option("--user-quota-num-volumes", type=int)
@click.option("--user-quota-ram-mb", type=int)
@click.option("--user-quota-volumes-gb", type=int)
@pass_api
def update(
    api: APIRequest,
    region_id,
    banner,
    description,
    download_server,
    enabled,
    lifespan_length,
    location,
    name,
    owner_group,
    reservation_expiration_max,
    reservations_enabled,
    tower_id,
    users_group,
    vault_server,
    dns_server_hostname,
    dns_server_key,
    dns_server_zone,
    openstack_credentials,
    openstack_domain_id,
    openstack_domain_name,
    openstack_keyname,
    openstack_networks_item,
    openstack_project,
    openstack_url,
    satellite_credentials,
    satellite_hostname,
    satellite_insecure,
    total_quota_num_vcpus,
    total_quota_num_volumes,
    total_quota_ram_mb,
    total_quota_volumes_gb,
    user_quota_num_vcpus,
    user_quota_num_volumes,
    user_quota_ram_mb,
    user_quota_volumes_gb,
):
    """Update region"""

    openstack_networks = []
    if openstack_networks_item is not None:
        openstack_networks.append(openstack_networks_item)

    user_quota = RhubApiLabRegionUpdateRegionJsonBodyUserQuota(
        num_vcpus=user_quota_num_vcpus,
        num_volumes=user_quota_num_volumes,
        ram_mb=user_quota_ram_mb,
        volumes_gb=user_quota_volumes_gb,
    )

    total_quota = RhubApiLabRegionUpdateRegionJsonBodyTotalQuota(
        num_vcpus=total_quota_num_vcpus,
        num_volumes=total_quota_num_volumes,
        ram_mb=total_quota_ram_mb,
        volumes_gb=total_quota_volumes_gb,
    )

    satellite = RhubApiLabRegionUpdateRegionJsonBodySatellite(
        credentials=satellite_credentials,
        hostname=satellite_hostname,
        insecure=satellite_insecure,
    )

    openstack = RhubApiLabRegionUpdateRegionJsonBodyOpenstack(
        credentials=openstack_credentials,
        domain_id=openstack_domain_id,
        domain_name=openstack_domain_name,
        keyname=openstack_keyname,
        networks=openstack_networks,
        project=openstack_project,
        url=openstack_url,
    )

    dns_server = RhubApiLabRegionUpdateRegionJsonBodyDnsServer(
        hostname=dns_server_hostname,
        key=dns_server_key,
        zone=dns_server_zone,
    )

    json_body = RhubApiLabRegionUpdateRegionJsonBody(
        banner=banner,
        description=description,
        dns_server=dns_server,
        download_server=download_server,
        enabled=enabled,
        lifespan_length=lifespan_length,
        location=location,
        name=name,
        openstack=openstack,
        owner_group=owner_group,
        reservation_expiration_max=reservation_expiration_max,
        reservations_enabled=reservations_enabled,
        satellite=satellite,
        total_quota=total_quota,
        tower_id=tower_id,
        user_quota=user_quota,
        users_group=users_group,
        vault_server=vault_server,
    )

    response = region_update(
        region_id=region_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


region.add_command(products)
region.add_command(usage)
