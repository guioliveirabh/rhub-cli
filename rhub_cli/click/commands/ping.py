import click

from rhub_cli.click.api_request import APIRequest, pass_api


@click.group(invoke_without_command=True)
@pass_api
@click.pass_context
def ping(context, api: APIRequest):
    """Pings the API."""
    if context.invoked_subcommand is None:
        api.get('ping')


@ping.command()
@pass_api
def get(api: APIRequest):
    """Pings the API."""
    api.get('ping')
