import click


@click.group()
def stdout():
    pass


@stdout.command()
@click.argument("event_id", type=int)
def get(
    event_id,
):
    """Get cluster event output"""
