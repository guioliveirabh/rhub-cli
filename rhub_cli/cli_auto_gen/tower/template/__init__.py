import click

from .jobs import jobs
from .launch import launch


@click.group()
def template():
    pass


@template.command()
def get_list():
    """Get list of Tower templates"""


@template.command()
def create():
    """Create Tower template"""


@template.command()
@click.argument("template_id", type=int)
def get(
    template_id,
):
    """Get Tower template"""


@template.command()
@click.argument("template_id", type=int)
def remove(
    template_id,
):
    """Delete Tower template"""


@template.command()
@click.argument("template_id", type=int)
def update(
    template_id,
):
    """Change Tower template"""


template.add_command(jobs)
template.add_command(launch)
