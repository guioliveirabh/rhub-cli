import click


@click.group()
def groups():
    pass


@groups.command()
@click.argument("user_id", type=str)
def get_list(
    user_id,
):
    """Get user groups"""


@groups.command()
@click.argument("user_id", type=str)
def create(
    user_id,
):
    """Add user to group"""


@groups.command()
@click.argument("user_id", type=str)
def remove(
    user_id,
):
    """Remove user from group"""
