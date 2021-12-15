import click

from .regions import regions


@click.group()
def product():
    pass


@product.command()
def get_list():
    """Get product list"""


@product.command()
def create():
    """Create product"""


@product.command()
@click.argument("product_id", type=int)
def get(
    product_id,
):
    """Get product"""


@product.command()
@click.argument("product_id", type=int)
def remove(
    product_id,
):
    """Delete product"""


@product.command()
@click.argument("product_id", type=int)
def update(
    product_id,
):
    """Update product"""


product.add_command(regions)
