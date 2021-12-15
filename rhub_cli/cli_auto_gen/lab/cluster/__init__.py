import click

from .events import events
from .hosts import hosts


@click.group()
def cluster():
    pass


@cluster.command()
def get_list():
    """Get cluster list"""


@cluster.command()
def create():
    """Create cluster"""


@cluster.command()
@click.argument("cluster_id", type=int)
def get(
    cluster_id,
):
    """Get cluster"""


@cluster.command()
@click.argument("cluster_id", type=int)
def remove(
    cluster_id,
):
    """Delete cluster"""


@cluster.command()
@click.argument("cluster_id", type=int)
def update(
    cluster_id,
):
    """Update cluster"""


cluster.add_command(events)
cluster.add_command(hosts)
