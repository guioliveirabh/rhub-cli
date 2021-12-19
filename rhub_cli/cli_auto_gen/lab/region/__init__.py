import click

from rhub_cli.api.lab.rhubapilabregioncreate_region import sync_detailed as region_create
from rhub_cli.api.lab.rhubapilabregiondelete_region import sync_detailed as region_remove
from rhub_cli.api.lab.rhubapilabregionget_region import sync_detailed as region_get
from rhub_cli.api.lab.rhubapilabregionlist_regions import sync_detailed as region_get_list
from rhub_cli.api.lab.rhubapilabregionupdate_region import sync_detailed as region_update
from rhub_cli.api_request import APIRequest, pass_api

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
@pass_api
def create(
    api: APIRequest,
):
    """Create region"""
    # TODO: json_body

    response = region_create(
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
@pass_api
def update(
    api: APIRequest,
    region_id,
):
    """Update region"""
    # TODO: json_body

    response = region_update(
        region_id=region_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


region.add_command(products)
