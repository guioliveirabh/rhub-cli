import json

import click

from rhub_cli.api.openstack.rhub_api_openstack_project_create import sync_detailed as project_create
from rhub_cli.api.openstack.rhub_api_openstack_project_delete import sync_detailed as project_remove
from rhub_cli.api.openstack.rhub_api_openstack_project_get import sync_detailed as project_get
from rhub_cli.api.openstack.rhub_api_openstack_project_list import sync_detailed as project_get_list
from rhub_cli.api.openstack.rhub_api_openstack_project_update import sync_detailed as project_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_openstack_project_create_json_body import RhubApiOpenstackProjectCreateJsonBody
from rhub_cli.models.rhub_api_openstack_project_create_json_body_id import RhubApiOpenstackProjectCreateJsonBodyId
from rhub_cli.models.rhub_api_openstack_project_list_filter import RhubApiOpenstackProjectListFilter
from rhub_cli.models.rhub_api_openstack_project_list_sort import RhubApiOpenstackProjectListSort
from rhub_cli.models.rhub_api_openstack_project_update_json_body import RhubApiOpenstackProjectUpdateJsonBody
from rhub_cli.models.rhub_api_openstack_project_update_json_body_id import RhubApiOpenstackProjectUpdateJsonBodyId
from rhub_cli.types import UNSET

from .limits import limits


@click.group()
def project():
    pass


@project.command()
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-cloud-id", type=int, help="ID of the cloud.")
@click.option(
    "--filter-name",
    type=str,
    help="Name of a project. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@click.option("--filter-owner-id", type=str)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_cloud_id,
    filter_name,
    filter_owner_id,
):
    """Get OpenStack project list"""

    if sort is not None:
        sort = RhubApiOpenstackProjectListSort(sort)

    filter_ = RhubApiOpenstackProjectListFilter(
        cloud_id=filter_cloud_id,
        name=filter_name,
        owner_id=filter_owner_id,
    )

    response = project_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@project.command()
@click.option("--cloud-id", required=True, type=int)
@click.option("--name", required=True, type=str)
@click.option("--cloud-name", type=str)
@click.option("--description", type=str)
@click.option("--group-id", type=str)
@click.option("--group-name", type=str)
@click.option("--id")
@click.option("--owner-id", type=str, help="Defaults to user who created a project.")
@click.option("--owner-name", type=str)
@pass_api
def create(
    api: APIRequest,
    cloud_id,
    name,
    cloud_name,
    description,
    group_id,
    group_name,
    id,
    owner_id,
    owner_name,
):
    """Create OpenStack project"""

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiOpenstackProjectCreateJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    json_body = RhubApiOpenstackProjectCreateJsonBody(
        cloud_id=cloud_id,
        name=name,
        cloud_name=cloud_name,
        description=description,
        group_id=group_id,
        group_name=group_name,
        id=id,
        owner_id=owner_id,
        owner_name=owner_name,
    )

    response = project_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@project.command()
@click.argument("project_id", type=int)
@pass_api
def get(
    api: APIRequest,
    project_id,
):
    """Get OpenStack project"""

    response = project_get(
        project_id=project_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@project.command()
@click.argument("project_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    project_id,
):
    """Delete OpenStack project"""

    response = project_remove(
        project_id=project_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@project.command()
@click.argument("project_id", type=int)
@click.option("--cloud-id", type=int)
@click.option("--cloud-name", type=str)
@click.option("--description", type=str)
@click.option("--group-id", type=str)
@click.option("--group-name", type=str)
@click.option("--id")
@click.option("--name", type=str)
@click.option("--owner-id", type=str, help="Defaults to user who created a project.")
@click.option("--owner-name", type=str)
@pass_api
def update(
    api: APIRequest,
    project_id,
    cloud_id,
    cloud_name,
    description,
    group_id,
    group_name,
    id,
    name,
    owner_id,
    owner_name,
):
    """Update OpenStack project"""

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiOpenstackProjectUpdateJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    json_body = RhubApiOpenstackProjectUpdateJsonBody(
        cloud_id=cloud_id,
        cloud_name=cloud_name,
        description=description,
        group_id=group_id,
        group_name=group_name,
        id=id,
        name=name,
        owner_id=owner_id,
        owner_name=owner_name,
    )

    response = project_update(
        project_id=project_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


project.add_command(limits)
