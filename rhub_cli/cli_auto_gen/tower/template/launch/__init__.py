import click


@click.group()
def launch():
    pass


@launch.command()
@click.argument("template_id", type=int)
def create(
    template_id,
):
    """Launch Tower template"""
