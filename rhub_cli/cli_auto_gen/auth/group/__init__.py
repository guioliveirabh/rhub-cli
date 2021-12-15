import click

from .roles import roles
from .users import users


@click.group()
def group():
    pass


@group.command()
def get_list():
    pass


@group.command()
def create():
    pass


@group.command()
def get():
    pass


@group.command()
def remove():
    pass


@group.command()
def update():
    pass


group.add_command(roles)
group.add_command(users)
