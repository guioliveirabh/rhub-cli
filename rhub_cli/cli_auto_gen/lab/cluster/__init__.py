import click

from .events import events
from .hosts import hosts


@click.group()
def cluster():
    pass


@cluster.command()
def get_list():
    pass


@cluster.command()
def create():
    pass


@cluster.command()
def get():
    pass


@cluster.command()
def remove():
    pass


@cluster.command()
def update():
    pass


cluster.add_command(events)
cluster.add_command(hosts)
