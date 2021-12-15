import click


@click.group()
def products():
    pass


@products.command()
@click.argument("region_id", type=int)
def get_list(
    region_id,
):
    """Get list of products that can be installed in the selected region."""


@products.command()
@click.argument("region_id", type=int)
def create(
    region_id,
):
    """Add product to region or disable/enable product in region"""


@products.command()
@click.argument("region_id", type=int)
def remove(
    region_id,
):
    """Remove product from region"""
