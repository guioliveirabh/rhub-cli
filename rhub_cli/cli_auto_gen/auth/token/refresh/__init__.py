import click


@click.group()
def refresh():
    pass


@refresh.command()
def create():
    """Refresh token"""
