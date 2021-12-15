import click


@click.group()
def stdout():
    pass


@stdout.command()
@click.argument("job_id", type=int)
def get(
    job_id,
):
    """Get stdout of Tower job"""
