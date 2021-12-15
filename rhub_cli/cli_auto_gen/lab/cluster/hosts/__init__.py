import click


@click.group()
def hosts():
    pass


@hosts.command()
@click.argument("cluster_id", type=int)
def get_list(
    cluster_id,
):
    """Get cluster hosts"""


@hosts.command()
@click.argument("cluster_id", type=int)
def create(
    cluster_id,
):
    """Create or update cluster hosts"""


@hosts.command()
@click.argument("cluster_id", type=int)
def remove(
    cluster_id,
):
    """Delete cluster hosts"""
