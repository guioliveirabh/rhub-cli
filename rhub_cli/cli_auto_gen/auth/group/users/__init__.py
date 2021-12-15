import click


@click.group()
def users():
    pass


@users.command()
def get_list():
    pass
