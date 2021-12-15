import click


@click.group()
def server():
    pass


@server.command()
def get_list():
    """Get list of Tower servers"""


@server.command()
def create():
    """Create Tower server"""


@server.command()
@click.argument("server_id", type=int)
def get(
    server_id,
):
    """Get Tower server"""


@server.command()
@click.argument("server_id", type=int)
def remove(
    server_id,
):
    """"""


@server.command()
@click.argument("server_id", type=int)
def update(
    server_id,
):
    """Change Tower server"""
