import click


@click.group()
def hosts():
    pass


@hosts.command()
def get_list():
    pass


@hosts.command()
def create():
    pass


@hosts.command()
def remove():
    pass
