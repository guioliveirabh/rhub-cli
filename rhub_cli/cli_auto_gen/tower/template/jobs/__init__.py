import click


@click.group()
def jobs():
    pass


@jobs.command()
def get_list():
    pass
