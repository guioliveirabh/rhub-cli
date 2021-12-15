import click

from .products import products


@click.group()
def region():
    pass


@region.command()
def get_list():
    """Get region list"""


@region.command()
def create():
    """Create region"""


@region.command()
@click.argument("region_id", type=int)
def get(
    region_id,
):
    """Get region"""


@region.command()
@click.argument("region_id", type=int)
def remove(
    region_id,
):
    """Delete region"""


@region.command()
@click.argument("region_id", type=int)
def update(
    region_id,
):
    """Update region"""


region.add_command(products)
