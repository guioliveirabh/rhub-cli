import click

from .relaunch import relaunch
from .stdout import stdout


@click.group()
def job():
    pass


@job.command()
def get_list():
    """List Tower jobs"""


@job.command()
@click.argument("job_id", type=int)
def get(
    job_id,
):
    """Get Tower job"""


job.add_command(relaunch)
job.add_command(stdout)
