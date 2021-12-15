import click


@click.group()
def relaunch():
    pass


@relaunch.command()
@click.argument("job_id", type=int)
def create(
    job_id,
):
    """Re-launch Tower job"""
