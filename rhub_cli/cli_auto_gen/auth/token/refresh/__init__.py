import click

from rhub_cli.api.auth.rhub_api_auth_token_refresh_token import sync_detailed as refresh_create
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def refresh():
    pass


@refresh.command()
@pass_api
def create(
    api: APIRequest,
):
    """Refresh token"""

    # TODO: header_parameters

    response = refresh_create(
        client=api.client,
    )
    api.handle_response(response)
