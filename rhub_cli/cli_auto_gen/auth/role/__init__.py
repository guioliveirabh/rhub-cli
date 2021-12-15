import click


@click.group()
def role():
    pass


@role.command()
def get_list():
    """Get role list"""


@role.command()
def create():
    """Create role"""


@role.command()
@click.argument("role_id", type=str)
def get(
    role_id,
):
    """Get role"""


@role.command()
@click.argument("role_id", type=str)
def remove(
    role_id,
):
    """Delete role"""


@role.command()
@click.argument("role_id", type=str)
def update(
    role_id,
):
    """Update role"""
