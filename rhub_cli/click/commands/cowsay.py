import click

from rhub_cli.click.api_request import APIRequest, pass_api


@click.group(invoke_without_command=True)
@pass_api
@click.pass_context
def cowsay(context, api: APIRequest):
    """Cows the API."""
    if context.invoked_subcommand is None:
        api.get('cowsay')


@cowsay.command()
@pass_api
def get(api: APIRequest):
    """Cows the API."""
    api.get('cowsay')
