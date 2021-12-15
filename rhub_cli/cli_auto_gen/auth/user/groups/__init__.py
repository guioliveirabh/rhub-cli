import click


@click.group()
def groups():
    pass


@groups.command()
def get_list():
    pass


@groups.command()
def create():
    pass


@groups.command()
def remove():
    pass
