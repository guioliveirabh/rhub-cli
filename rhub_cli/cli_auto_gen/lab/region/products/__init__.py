import click

from rhub_cli.api.lab.rhubapilabregionadd_region_product import sync_detailed as products_create
from rhub_cli.api.lab.rhubapilabregiondelete_region_product import sync_detailed as products_remove
from rhub_cli.api.lab.rhubapilabregionlist_region_products import sync_detailed as products_get_list
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def products():
    pass


@products.command()
@click.argument("region_id", type=int)
@pass_api
def get_list(
    api: APIRequest,
    region_id,
):
    """Get list of products that can be installed in the selected region."""
    # TODO: query_parameters

    response = products_get_list(
        region_id=region_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@products.command()
@click.argument("region_id", type=int)
@pass_api
def create(
    api: APIRequest,
    region_id,
):
    """Add product to region or disable/enable product in region"""
    # TODO: json_body

    response = products_create(
        region_id=region_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@products.command()
@click.argument("region_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    region_id,
):
    """Remove product from region"""
    # TODO: json_body

    response = products_remove(
        region_id=region_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
