import click

from .stdout import stdout


@click.group()
def cluster_event():
    pass


@cluster_event.command()
@click.argument("event_id", type=int)
def get(
    event_id,
):
    """Get cluster event"""


cluster_event.add_command(stdout)
