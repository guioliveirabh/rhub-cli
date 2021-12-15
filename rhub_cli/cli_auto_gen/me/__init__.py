import click


@click.group()
def me():
    pass


@me.command()
def get():
    """Get info about logged in user"""
