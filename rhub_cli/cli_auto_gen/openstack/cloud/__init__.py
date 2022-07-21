import json

import click

from rhub_cli.api.openstack.rhub_api_openstack_cloud_create import sync_detailed as cloud_create
from rhub_cli.api.openstack.rhub_api_openstack_cloud_delete import sync_detailed as cloud_remove
from rhub_cli.api.openstack.rhub_api_openstack_cloud_get import sync_detailed as cloud_get
from rhub_cli.api.openstack.rhub_api_openstack_cloud_list import sync_detailed as cloud_get_list
from rhub_cli.api.openstack.rhub_api_openstack_cloud_update import sync_detailed as cloud_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_openstack_cloud_create_json_body import RhubApiOpenstackCloudCreateJsonBody
from rhub_cli.models.rhub_api_openstack_cloud_create_json_body_id import RhubApiOpenstackCloudCreateJsonBodyId
from rhub_cli.models.rhub_api_openstack_cloud_list_filter import RhubApiOpenstackCloudListFilter
from rhub_cli.models.rhub_api_openstack_cloud_list_sort import RhubApiOpenstackCloudListSort
from rhub_cli.models.rhub_api_openstack_cloud_update_json_body import RhubApiOpenstackCloudUpdateJsonBody
from rhub_cli.models.rhub_api_openstack_cloud_update_json_body_id import RhubApiOpenstackCloudUpdateJsonBodyId
from rhub_cli.types import UNSET


@click.group()
def cloud():
    pass


@cloud.command()
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option(
    "--filter-name",
    type=str,
    help="Name of a cloud. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@click.option("--filter-owner-group-id", type=str)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_name,
    filter_owner_group_id,
):
    """Get OpenStack cloud list"""

    if sort is not None:
        sort = RhubApiOpenstackCloudListSort(sort)

    filter_ = RhubApiOpenstackCloudListFilter(
        name=filter_name,
        owner_group_id=filter_owner_group_id,
    )

    response = cloud_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cloud.command()
@click.option("--credentials", required=True)
@click.option("--domain-id", required=True, type=str)
@click.option("--domain-name", required=True, type=str)
@click.option("--name", required=True, type=str)
@click.option("--networks-item", required=True, type=str)
@click.option("--owner-group-id", required=True, type=str)
@click.option("--url", required=True, type=str)
@click.option("--description", type=str)
@click.option("--id")
@click.option("--owner-group-name", type=str)
@pass_api
def create(
    api: APIRequest,
    credentials,
    domain_id,
    domain_name,
    name,
    networks_item,
    owner_group_id,
    url,
    description,
    id,
    owner_group_name,
):
    """Create OpenStack cloud"""

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiOpenstackCloudCreateJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    networks = []
    if networks_item is not None:
        networks.append(networks_item)

    json_body = RhubApiOpenstackCloudCreateJsonBody(
        credentials=credentials,
        domain_id=domain_id,
        domain_name=domain_name,
        name=name,
        networks=networks,
        owner_group_id=owner_group_id,
        url=url,
        description=description,
        id=id,
        owner_group_name=owner_group_name,
    )

    response = cloud_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cloud.command()
@click.argument("cloud_id", type=int)
@pass_api
def get(
    api: APIRequest,
    cloud_id,
):
    """Get OpenStack cloud"""

    response = cloud_get(
        cloud_id=cloud_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cloud.command()
@click.argument("cloud_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    cloud_id,
):
    """Delete OpenStack cloud"""

    response = cloud_remove(
        cloud_id=cloud_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cloud.command()
@click.argument("cloud_id", type=int)
@click.option("--credentials")
@click.option("--description", type=str)
@click.option("--domain-id", type=str)
@click.option("--domain-name", type=str)
@click.option("--id")
@click.option("--name", type=str)
@click.option("--networks-item", type=str)
@click.option("--owner-group-id", type=str)
@click.option("--owner-group-name", type=str)
@click.option("--url", type=str)
@pass_api
def update(
    api: APIRequest,
    cloud_id,
    credentials,
    description,
    domain_id,
    domain_name,
    id,
    name,
    networks_item,
    owner_group_id,
    owner_group_name,
    url,
):
    """Update OpenStack cloud"""

    networks = []
    if networks_item is not None:
        networks.append(networks_item)

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiOpenstackCloudUpdateJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    json_body = RhubApiOpenstackCloudUpdateJsonBody(
        credentials=credentials,
        description=description,
        domain_id=domain_id,
        domain_name=domain_name,
        id=id,
        name=name,
        networks=networks,
        owner_group_id=owner_group_id,
        owner_group_name=owner_group_name,
        url=url,
    )

    response = cloud_update(
        cloud_id=cloud_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
