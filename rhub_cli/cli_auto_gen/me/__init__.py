import click


@click.group()
def me():
    pass


@me.command()
def get():
    pass
