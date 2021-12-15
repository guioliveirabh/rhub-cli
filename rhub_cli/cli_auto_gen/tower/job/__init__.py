import click

from .relaunch import relaunch
from .stdout import stdout


@click.group()
def job():
    pass


@job.command()
def get_list():
    pass


@job.command()
def get():
    pass


job.add_command(relaunch)
job.add_command(stdout)
