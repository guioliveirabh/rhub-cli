import click

from .products import products


@click.group()
def region():
    pass


@region.command()
def get_list():
    pass


@region.command()
def create():
    pass


@region.command()
def get():
    pass


@region.command()
def remove():
    pass


@region.command()
def update():
    pass


region.add_command(products)
