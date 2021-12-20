from typing import Any, List

import click

from rhub_cli.api.lab.rhubapilabproductcreate_product import sync_detailed as product_create
from rhub_cli.api.lab.rhubapilabproductdelete_product import sync_detailed as product_remove
from rhub_cli.api.lab.rhubapilabproductget_product import sync_detailed as product_get
from rhub_cli.api.lab.rhubapilabproductlist_products import sync_detailed as product_get_list
from rhub_cli.api.lab.rhubapilabproductupdate_product import sync_detailed as product_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapilabproductcreate_product_json_body import RhubapilabproductcreateProductJsonBody
from rhub_cli.models.rhubapilabproductupdate_product_json_body import RhubapilabproductupdateProductJsonBody

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
@click.option("--name", required=True, type=str)
@click.option("--parameters", required=True, type=List[Any])
@click.option("--tower-template-name-create", required=True, type=str)
@click.option("--tower-template-name-delete", required=True, type=str)
@click.option("--description", type=str)
@click.option("--enabled", type=bool)
@pass_api
def create(
    api: APIRequest,
    name,
    parameters,
    tower_template_name_create,
    tower_template_name_delete,
    description,
    enabled,
):
    """Create product"""
    json_body = RhubapilabproductcreateProductJsonBody(
        name=name,
        parameters=parameters,
        tower_template_name_create=tower_template_name_create,
        tower_template_name_delete=tower_template_name_delete,
        description=description,
        enabled=enabled,
    )

    response = product_create(
        json_body=json_body,
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
@click.option("--description", type=str)
@click.option("--enabled", type=bool)
@click.option("--name", type=str)
@click.option("--parameters", type=List[Any])
@click.option("--tower-template-name-create", type=str)
@click.option("--tower-template-name-delete", type=str)
@pass_api
def update(
    api: APIRequest,
    product_id,
    description,
    enabled,
    name,
    parameters,
    tower_template_name_create,
    tower_template_name_delete,
):
    """Update product"""
    json_body = RhubapilabproductupdateProductJsonBody(
        description=description,
        enabled=enabled,
        name=name,
        parameters=parameters,
        tower_template_name_create=tower_template_name_create,
        tower_template_name_delete=tower_template_name_delete,
    )

    response = product_update(
        product_id=product_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


product.add_command(regions)
