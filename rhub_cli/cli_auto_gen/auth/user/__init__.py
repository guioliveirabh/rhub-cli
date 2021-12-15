import click

from .groups import groups
from .roles import roles


@click.group()
def user():
    pass


@user.command()
def get_list():
    pass


@user.command()
def create():
    pass


@user.command()
def get():
    pass


@user.command()
def remove():
    pass


@user.command()
def update():
    pass


user.add_command(groups)
user.add_command(roles)
