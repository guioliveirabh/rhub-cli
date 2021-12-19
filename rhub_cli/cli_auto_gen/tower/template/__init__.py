import click

from rhub_cli.api.tower.rhubapitowercreate_template import sync_detailed as template_create
from rhub_cli.api.tower.rhubapitowerdelete_template import sync_detailed as template_remove
from rhub_cli.api.tower.rhubapitowerget_template import sync_detailed as template_get
from rhub_cli.api.tower.rhubapitowerlist_templates import sync_detailed as template_get_list
from rhub_cli.api.tower.rhubapitowerupdate_template import sync_detailed as template_update
from rhub_cli.api_request import APIRequest, pass_api

from .jobs import jobs
from .launch import launch


@click.group()
def template():
    pass


@template.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get list of Tower templates"""
    # TODO: query_parameters

    response = template_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@template.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create Tower template"""
    # TODO: json_body

    response = template_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@template.command()
@click.argument("template_id", type=int)
@pass_api
def get(
    api: APIRequest,
    template_id,
):
    """Get Tower template"""

    response = template_get(
        template_id=template_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@template.command()
@click.argument("template_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    template_id,
):
    """Delete Tower template"""

    response = template_remove(
        template_id=template_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@template.command()
@click.argument("template_id", type=int)
@pass_api
def update(
    api: APIRequest,
    template_id,
):
    """Change Tower template"""
    # TODO: json_body

    response = template_update(
        template_id=template_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


template.add_command(jobs)
template.add_command(launch)
