import click

from rhub_cli.api.tower.rhubapitowerlaunch_template import sync_detailed as launch_create
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def launch():
    pass


@launch.command()
@click.argument("template_id", type=int)
@pass_api
def create(
    api: APIRequest,
    template_id,
):
    """Launch Tower template"""
    # TODO: json_body

    response = launch_create(
        template_id=template_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
