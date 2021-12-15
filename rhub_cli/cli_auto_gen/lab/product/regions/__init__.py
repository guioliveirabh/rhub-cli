import click


@click.group()
def regions():
    pass


@regions.command()
def get_list():
    pass
