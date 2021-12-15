import click

from .groups import groups
from .roles import roles


@click.group()
def user():
    pass


@user.command()
def get_list():
    """Get user list"""


@user.command()
def create():
    """Create user"""


@user.command()
@click.argument("user_id", type=str)
def get(
    user_id,
):
    """Get user"""


@user.command()
@click.argument("user_id", type=str)
def remove(
    user_id,
):
    """Delete user"""


@user.command()
@click.argument("user_id", type=str)
def update(
    user_id,
):
    """Update user"""


user.add_command(groups)
user.add_command(roles)
