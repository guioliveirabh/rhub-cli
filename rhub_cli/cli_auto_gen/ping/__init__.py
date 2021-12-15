import click


@click.group()
def ping():
    pass


@ping.command()
def get():
    """Basic availablity endpoint"""
