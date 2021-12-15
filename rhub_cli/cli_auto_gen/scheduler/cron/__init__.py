import click



@click.group()
def cron():
    pass


@cron.command()
def get_list():
    pass


@cron.command()
def create():
    pass


@cron.command()
def get():
    pass


@cron.command()
def remove():
    pass


@cron.command()
def update():
    pass


