import click

from .create import create
from .refresh import refresh


@click.group()
def token():
    pass


@token.command()
def get():
    """Get auth token info"""


token.add_command(create)
token.add_command(refresh)
