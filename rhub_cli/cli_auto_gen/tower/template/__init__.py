import click

from .jobs import jobs
from .launch import launch


@click.group()
def template():
    pass


@template.command()
def get_list():
    pass


@template.command()
def create():
    pass


@template.command()
def get():
    pass


@template.command()
def remove():
    pass


@template.command()
def update():
    pass


template.add_command(jobs)
template.add_command(launch)
