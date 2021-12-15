import click


@click.group()
def stdout():
    pass


@stdout.command()
def get():
    pass
