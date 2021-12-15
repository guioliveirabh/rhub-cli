import click



@click.group()
def policies():
    pass


@policies.command()
def get_list():
    pass


@policies.command()
def create():
    pass


@policies.command()
def get():
    pass


@policies.command()
def remove():
    pass


@policies.command()
def update():
    pass


