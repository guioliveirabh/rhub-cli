import click

from .create import create
from .refresh import refresh


@click.group()
def token():
    pass


@token.command()
def get():
    pass


token.add_command(create)
token.add_command(refresh)
