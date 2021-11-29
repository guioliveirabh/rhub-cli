import click
import pkg_resources

from rhub_cli.click import commands
from rhub_cli.click.api_request import APIRequest

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    show_default=True,
)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--base-url',  # TODO: add type
              envvar='BASE_URL',
              metavar='URL',
              default='http://localhost:8081/v0',  # TODO: replace
              help='Base URL used for API calls.')
@click.option('--verbose', '-v', is_flag=True, help='Enables verbose mode.')
@click.version_option(pkg_resources.require('rhub_cli')[0].version)
@click.pass_context
def cli(context, base_url: str, verbose: bool):
    """CLI example using Click - https://click.palletsprojects.com/"""
    context.obj = APIRequest(base_url)


cli.add_command(commands.cowsay)
cli.add_command(commands.ping)
cli.add_command(commands.policies)
