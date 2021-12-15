import click


@click.group()
def regions():
    pass


@regions.command()
@click.argument("product_id", type=int)
def get_list(
    product_id,
):
    """Get list of regions where product can be installed."""
