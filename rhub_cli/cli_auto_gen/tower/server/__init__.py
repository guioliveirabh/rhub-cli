import click


@click.group()
def server():
    pass


@server.command()
def get_list():
    pass


@server.command()
def create():
    pass


@server.command()
def get():
    pass


@server.command()
def remove():
    pass


@server.command()
def update():
    pass
