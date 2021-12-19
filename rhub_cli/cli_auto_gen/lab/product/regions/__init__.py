import click

from rhub_cli.api.lab.rhubapilabproductlist_product_regions import sync_detailed as regions_get_list
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def regions():
    pass


@regions.command()
@click.argument("product_id", type=int)
@pass_api
def get_list(
    api: APIRequest,
    product_id,
):
    """Get list of regions where product can be installed."""
    # TODO: query_parameters

    response = regions_get_list(
        product_id=product_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
