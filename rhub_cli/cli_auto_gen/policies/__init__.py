import click


@click.group()
def policies():
    pass


@policies.command()
def get_list():
    """Get policy list"""


@policies.command()
def create():
    """Create policy"""


@policies.command()
@click.argument("policy_id", type=int)
def get(
    policy_id,
):
    """Get policy"""


@policies.command()
@click.argument("policy_id", type=int)
def remove(
    policy_id,
):
    """Delete policy"""


@policies.command()
@click.argument("policy_id", type=int)
def update(
    policy_id,
):
    """Update policy"""
