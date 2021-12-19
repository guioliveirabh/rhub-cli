import click

from .api_request import APIRequest

CONTEXT_SETTINGS = dict(
    help_option_names=["-h", "--help"],
    show_default=True,
)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--base-url",  # TODO: add type
    envvar="BASE_URL",
    metavar="URL",
    default="http://localhost:8081/v0",  # TODO: replace
    help="Base URL used for API calls.",
)
@click.option(
    "--user",
    default="testuser1",  # TODO: replace
    help="User used for authentication.",
)
@click.option(
    "--password",
    hide_input=True,
    default="testuser1",  # TODO: replace
    help="Password used for authentication.",
)
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
@click.version_option("0.1")
@click.pass_context
def cli(context, base_url: str, user: str, password: str, verbose: bool):
    """rhub-cli
    A client library for accessing Resource Hub"""
    context.obj = APIRequest(base_url=base_url, user=user, password=password, verbose=verbose)
