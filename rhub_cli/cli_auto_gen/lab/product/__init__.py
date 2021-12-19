import click

from rhub_cli.api.lab.rhubapilabproductcreate_product import sync_detailed as product_create
from rhub_cli.api.lab.rhubapilabproductdelete_product import sync_detailed as product_remove
from rhub_cli.api.lab.rhubapilabproductget_product import sync_detailed as product_get
from rhub_cli.api.lab.rhubapilabproductlist_products import sync_detailed as product_get_list
from rhub_cli.api.lab.rhubapilabproductupdate_product import sync_detailed as product_update
from rhub_cli.api_request import APIRequest, pass_api

from .regions import regions


@click.group()
def product():
    pass


@product.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get product list"""
    # TODO: query_parameters

    response = product_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@product.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create product"""
    # TODO: json_body

    response = product_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@product.command()
@click.argument("product_id", type=int)
@pass_api
def get(
    api: APIRequest,
    product_id,
):
    """Get product"""

    response = product_get(
        product_id=product_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@product.command()
@click.argument("product_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    product_id,
):
    """Delete product"""

    response = product_remove(
        product_id=product_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@product.command()
@click.argument("product_id", type=int)
@pass_api
def update(
    api: APIRequest,
    product_id,
):
    """Update product"""
    # TODO: json_body

    response = product_update(
        product_id=product_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


product.add_command(regions)
