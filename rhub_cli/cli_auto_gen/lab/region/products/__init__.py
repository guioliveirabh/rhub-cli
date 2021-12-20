import click

from rhub_cli.api.lab.rhubapilabregionadd_region_product import sync_detailed as products_create
from rhub_cli.api.lab.rhubapilabregiondelete_region_product import sync_detailed as products_remove
from rhub_cli.api.lab.rhubapilabregionlist_region_products import sync_detailed as products_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapilabregionadd_region_product_json_body import RhubapilabregionaddRegionProductJsonBody
from rhub_cli.models.rhubapilabregiondelete_region_product_json_body import RhubapilabregiondeleteRegionProductJsonBody


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
@click.option("--id", required=True, type=int)
@click.option("--enabled", type=bool)
@pass_api
def create(
    api: APIRequest,
    region_id,
    id,
    enabled,
):
    """Add product to region or disable/enable product in region"""
    json_body = RhubapilabregionaddRegionProductJsonBody(
        id=id,
        enabled=enabled,
    )

    response = products_create(
        region_id=region_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@products.command()
@click.argument("region_id", type=int)
@click.option("--id", required=True, type=int)
@pass_api
def remove(
    api: APIRequest,
    region_id,
    id,
):
    """Remove product from region"""
    json_body = RhubapilabregiondeleteRegionProductJsonBody(
        id=id,
    )

    response = products_remove(
        region_id=region_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
