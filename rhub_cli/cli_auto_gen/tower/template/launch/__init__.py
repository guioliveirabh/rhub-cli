import click

from rhub_cli.api.tower.rhubapitowerlaunch_template import sync_detailed as launch_create
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapitowerlaunch_template_json_body import RhubapitowerlaunchTemplateJsonBody


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

    json_body = RhubapitowerlaunchTemplateJsonBody()

    response = launch_create(
        template_id=template_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
