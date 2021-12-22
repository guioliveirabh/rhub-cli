import click

from rhub_cli.api.tower.rhubapitowerget_job import sync_detailed as job_get
from rhub_cli.api.tower.rhubapitowerlist_jobs import sync_detailed as job_get_list
from rhub_cli.api_request import APIRequest, pass_api

from .relaunch import relaunch
from .stdout import stdout


@click.group()
def job():
    pass


@job.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """List Tower jobs"""

    # TODO: query_parameters

    response = job_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@job.command()
@click.argument("job_id", type=int)
@pass_api
def get(
    api: APIRequest,
    job_id,
):
    """Get Tower job"""

    response = job_get(
        job_id=job_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


job.add_command(relaunch)
job.add_command(stdout)
