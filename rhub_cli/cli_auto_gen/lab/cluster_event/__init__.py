import click

from .stdout import stdout


@click.group()
def cluster_event():
    pass


@cluster_event.command()
def get():
    pass


cluster_event.add_command(stdout)
