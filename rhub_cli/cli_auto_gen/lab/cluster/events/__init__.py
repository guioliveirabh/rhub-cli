import click


@click.group()
def events():
    pass


@events.command()
@click.argument("cluster_id", type=int)
def get_list(
    cluster_id,
):
    """Get cluster events list"""
