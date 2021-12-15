import click


@click.group()
def webhook_notification():
    pass


@webhook_notification.command()
def create():
    pass
