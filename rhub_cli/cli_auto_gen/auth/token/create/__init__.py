import click


@click.group()
def create():
    pass


@create.command()
def create():
    """Login and get access token"""
