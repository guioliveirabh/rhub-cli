import click


@click.group()
def roles():
    pass


@roles.command()
@click.argument("group_id", type=str)
def get_list(
    group_id,
):
    """Get group roles"""


@roles.command()
@click.argument("group_id", type=str)
def create(
    group_id,
):
    """Add group to role"""


@roles.command()
@click.argument("group_id", type=str)
def remove(
    group_id,
):
    """Remove group from role"""
