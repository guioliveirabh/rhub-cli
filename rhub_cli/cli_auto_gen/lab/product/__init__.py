import click

from rhub_cli.api.lab.rhub_api_lab_product_create_product import sync_detailed as product_create
from rhub_cli.api.lab.rhub_api_lab_product_delete_product import sync_detailed as product_remove
from rhub_cli.api.lab.rhub_api_lab_product_get_product import sync_detailed as product_get
from rhub_cli.api.lab.rhub_api_lab_product_list_products import sync_detailed as product_get_list
from rhub_cli.api.lab.rhub_api_lab_product_update_product import sync_detailed as product_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_product_create_product_json_body import RhubApiLabProductCreateProductJsonBody
from rhub_cli.models.rhub_api_lab_product_update_product_json_body import RhubApiLabProductUpdateProductJsonBody

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
@click.option("--name", type=str)
@click.option("--parameters", multiple=True)
@click.option("--tower-template-name-create", type=str)
@click.option("--tower-template-name-delete", type=str)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
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

    json_body = RhubApiLabProductCreateProductJsonBody(
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
@click.option("--enabled", is_flag=True)
@click.option("--name", type=str)
@click.option("--parameters", multiple=True)
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

    json_body = RhubApiLabProductUpdateProductJsonBody(
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
