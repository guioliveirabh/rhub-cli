import click

from .roles import roles
from .users import users


@click.group()
def group():
    pass


@group.command()
def get_list():
    """Get group list"""


@group.command()
def create():
    """Create group"""


@group.command()
@click.argument("group_id", type=str)
def get(
    group_id,
):
    """Get group"""


@group.command()
@click.argument("group_id", type=str)
def remove(
    group_id,
):
    """Delete group"""


@group.command()
@click.argument("group_id", type=str)
def update(
    group_id,
):
    """Update group"""


group.add_command(roles)
group.add_command(users)
