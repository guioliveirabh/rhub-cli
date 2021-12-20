import click

from rhub_cli.api.scheduler.rhubapischedulercroncreate_job import sync_detailed as cron_create
from rhub_cli.api.scheduler.rhubapischedulercrondelete_job import sync_detailed as cron_remove
from rhub_cli.api.scheduler.rhubapischedulercronget_job import sync_detailed as cron_get
from rhub_cli.api.scheduler.rhubapischedulercronlist_jobs import sync_detailed as cron_get_list
from rhub_cli.api.scheduler.rhubapischedulercronupdate_job import sync_detailed as cron_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapischedulercroncreate_job_json_body import RhubapischedulercroncreateJobJsonBody
from rhub_cli.models.rhubapischedulercronupdate_job_json_body import RhubapischedulercronupdateJobJsonBody


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
@click.option("--job-name", required=True, type=str)
@click.option("--name", required=True, type=str)
@click.option("--time-expr", required=True, type=str)
@click.option("--description", type=str)
@click.option("--enabled", type=bool)
@click.option("--last-run", type=str)
@pass_api
def create(
    api: APIRequest,
    job_name,
    name,
    time_expr,
    description,
    enabled,
    last_run,
):
    """Create CronJob"""
    json_body = RhubapischedulercroncreateJobJsonBody(
        job_name=job_name,
        name=name,
        time_expr=time_expr,
        description=description,
        enabled=enabled,
        last_run=last_run,
    )

    response = cron_create(
        json_body=json_body,
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
@click.option("--description", type=str)
@click.option("--enabled", type=bool)
@click.option("--job-name", type=str)
@click.option("--last-run", type=str)
@click.option("--name", type=str)
@click.option("--time-expr", type=str)
@pass_api
def update(
    api: APIRequest,
    cron_job_id,
    description,
    enabled,
    job_name,
    last_run,
    name,
    time_expr,
):
    """Update CronJob"""
    json_body = RhubapischedulercronupdateJobJsonBody(
        description=description,
        enabled=enabled,
        job_name=job_name,
        last_run=last_run,
        name=name,
        time_expr=time_expr,
    )

    response = cron_update(
        cron_job_id=cron_job_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
