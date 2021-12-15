import click



@click.group()
def role():
    pass


@role.command()
def get_list():
    pass


@role.command()
def create():
    pass


@role.command()
def get():
    pass


@role.command()
def remove():
    pass


@role.command()
def update():
    pass


