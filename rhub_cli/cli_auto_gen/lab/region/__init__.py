from typing import Any, Dict, List, Union

import click

from rhub_cli.api.lab.rhubapilabregioncreate_region import sync_detailed as region_create
from rhub_cli.api.lab.rhubapilabregiondelete_region import sync_detailed as region_remove
from rhub_cli.api.lab.rhubapilabregionget_region import sync_detailed as region_get
from rhub_cli.api.lab.rhubapilabregionlist_regions import sync_detailed as region_get_list
from rhub_cli.api.lab.rhubapilabregionupdate_region import sync_detailed as region_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapilabregioncreate_region_json_body import RhubapilabregioncreateRegionJsonBody
from rhub_cli.models.rhubapilabregionupdate_region_json_body import RhubapilabregionupdateRegionJsonBody

from .products import products


@click.group()
def region():
    pass


@region.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get region list"""
    # TODO: query_parameters

    response = region_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@region.command()
@click.option("--dns-server", required=True, type=Any)
@click.option("--download-server", required=True, type=str)
@click.option("--name", required=True, type=str)
@click.option("--openstack", required=True, type=Any)
@click.option("--satellite", required=True, type=Any)
@click.option("--tower-id", required=True, type=int)
@click.option("--vault-server", required=True, type=str)
@click.option("--banner", type=str)
@click.option("--description", type=str)
@click.option("--enabled", type=bool)
@click.option("--lifespan-length", type=int)
@click.option("--location", type=str)
@click.option("--owner-group", type=str)
@click.option("--quota", type=Union[Any, Dict[str, Any]])
@click.option("--reservation-expiration-max", type=int)
@click.option("--reservations-enabled", type=bool)
@click.option("--users-group", type=str)
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
    quota,
    reservation_expiration_max,
    reservations_enabled,
    users_group,
):
    """Create region"""
    json_body = RhubapilabregioncreateRegionJsonBody(
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
        quota=quota,
        reservation_expiration_max=reservation_expiration_max,
        reservations_enabled=reservations_enabled,
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
@click.option("--dns-server-hostname", type=str)
@click.option("--dns-server-key", type=Union[Dict[str, Any], str])
@click.option("--dns-server-zone", type=str)
@click.option("--download-server", type=str)
@click.option("--enabled", type=bool)
@click.option("--lifespan-length", type=int)
@click.option("--location", type=str)
@click.option("--name", type=str)
@click.option("--openstack-credentials", type=Union[Dict[str, Any], str])
@click.option("--openstack-domain-id", type=str)
@click.option("--openstack-domain-name", type=str)
@click.option("--openstack-keyname", type=str)
@click.option("--openstack-networks", type=List[str])
@click.option("--openstack-project", type=str)
@click.option("--openstack-url", type=str)
@click.option("--owner-group", type=str)
@click.option("--quota", type=Union[Any, Dict[str, Any]])
@click.option("--reservation-expiration-max", type=int)
@click.option("--reservations-enabled", type=bool)
@click.option("--satellite-credentials", type=Union[Dict[str, Any], str])
@click.option("--satellite-hostname", type=str)
@click.option("--satellite-insecure", type=bool)
@click.option("--tower-id", type=int)
@click.option("--users-group", type=str)
@click.option("--vault-server", type=str)
@pass_api
def update(
    api: APIRequest,
    region_id,
    banner,
    description,
    dns_server_hostname,
    dns_server_key,
    dns_server_zone,
    download_server,
    enabled,
    lifespan_length,
    location,
    name,
    openstack_credentials,
    openstack_domain_id,
    openstack_domain_name,
    openstack_keyname,
    openstack_networks,
    openstack_project,
    openstack_url,
    owner_group,
    quota,
    reservation_expiration_max,
    reservations_enabled,
    satellite_credentials,
    satellite_hostname,
    satellite_insecure,
    tower_id,
    users_group,
    vault_server,
):
    """Update region"""
    json_body = RhubapilabregionupdateRegionJsonBody(
        banner=banner,
        description=description,
        hostname=dns_server_hostname,
        key=dns_server_key,
        zone=dns_server_zone,
        download_server=download_server,
        enabled=enabled,
        lifespan_length=lifespan_length,
        location=location,
        name=name,
        credentials=openstack_credentials,
        domain_id=openstack_domain_id,
        domain_name=openstack_domain_name,
        keyname=openstack_keyname,
        networks=openstack_networks,
        project=openstack_project,
        url=openstack_url,
        owner_group=owner_group,
        quota=quota,
        reservation_expiration_max=reservation_expiration_max,
        reservations_enabled=reservations_enabled,
        # credentials=satellite_credentials,
        # hostname=satellite_hostname,
        insecure=satellite_insecure,
        tower_id=tower_id,
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
