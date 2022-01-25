import click

from rhub_cli.api.tower.rhub_api_tower_list_template_jobs import sync_detailed as jobs_get_list
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def jobs():
    pass


@jobs.command()
@click.argument("template_id", type=int)
@pass_api
def get_list(
    api: APIRequest,
    template_id,
):
    """List Tower template jobs"""

    # TODO: query_parameters

    response = jobs_get_list(
        template_id=template_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
