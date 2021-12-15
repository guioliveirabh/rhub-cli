import click


@click.group()
def jobs():
    pass


@jobs.command()
@click.argument("template_id", type=int)
def get_list(
    template_id,
):
    """List Tower template jobs"""
