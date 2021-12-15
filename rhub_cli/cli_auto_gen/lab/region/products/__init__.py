import click


@click.group()
def products():
    pass


@products.command()
def get_list():
    pass


@products.command()
def create():
    pass


@products.command()
def remove():
    pass
