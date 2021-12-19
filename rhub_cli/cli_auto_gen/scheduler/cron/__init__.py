import click

from rhub_cli.api.scheduler.rhubapischedulercroncreate_job import sync_detailed as cron_create
from rhub_cli.api.scheduler.rhubapischedulercrondelete_job import sync_detailed as cron_remove
from rhub_cli.api.scheduler.rhubapischedulercronget_job import sync_detailed as cron_get
from rhub_cli.api.scheduler.rhubapischedulercronlist_jobs import sync_detailed as cron_get_list
from rhub_cli.api.scheduler.rhubapischedulercronupdate_job import sync_detailed as cron_update
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def cron():
    pass


@cron.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get CronJob list"""
    # TODO: query_parameters

    response = cron_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cron.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create CronJob"""
    # TODO: json_body

    response = cron_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cron.command()
@click.argument("cron_job_id", type=int)
@pass_api
def get(
    api: APIRequest,
    cron_job_id,
):
    """Get CronJob"""

    response = cron_get(
        cron_job_id=cron_job_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cron.command()
@click.argument("cron_job_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    cron_job_id,
):
    """Delete CronJob"""

    response = cron_remove(
        cron_job_id=cron_job_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cron.command()
@click.argument("cron_job_id", type=int)
@pass_api
def update(
    api: APIRequest,
    cron_job_id,
):
    """Update CronJob"""
    # TODO: json_body

    response = cron_update(
        cron_job_id=cron_job_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
