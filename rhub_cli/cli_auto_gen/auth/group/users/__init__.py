import click


@click.group()
def users():
    pass


@users.command()
@click.argument("group_id", type=str)
def get_list(
    group_id,
):
    """Get users in group"""
