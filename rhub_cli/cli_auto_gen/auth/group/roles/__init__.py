import click


@click.group()
def roles():
    pass


@roles.command()
def get_list():
    pass


@roles.command()
def create():
    pass


@roles.command()
def remove():
    pass
