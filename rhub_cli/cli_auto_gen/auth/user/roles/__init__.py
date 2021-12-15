import click


@click.group()
def roles():
    pass


@roles.command()
@click.argument("user_id", type=str)
def get_list(
    user_id,
):
    """Get user roles"""


@roles.command()
@click.argument("user_id", type=str)
def create(
    user_id,
):
    """Add user to role"""


@roles.command()
@click.argument("user_id", type=str)
def remove(
    user_id,
):
    """Remove user from role"""
