import click

from .regions import regions


@click.group()
def product():
    pass


@product.command()
def get_list():
    pass


@product.command()
def create():
    pass


@product.command()
def get():
    pass


@product.command()
def remove():
    pass


@product.command()
def update():
    pass


product.add_command(regions)
