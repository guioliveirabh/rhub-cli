import click

from rhub_cli.api.tower.rhub_api_tower_create_template import sync_detailed as template_create
from rhub_cli.api.tower.rhub_api_tower_delete_template import sync_detailed as template_remove
from rhub_cli.api.tower.rhub_api_tower_get_template import sync_detailed as template_get
from rhub_cli.api.tower.rhub_api_tower_list_templates import sync_detailed as template_get_list
from rhub_cli.api.tower.rhub_api_tower_update_template import sync_detailed as template_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_tower_create_template_json_body import RhubApiTowerCreateTemplateJsonBody
from rhub_cli.models.rhub_api_tower_list_templates_filter import RhubApiTowerListTemplatesFilter
from rhub_cli.models.rhub_api_tower_list_templates_sort import RhubApiTowerListTemplatesSort
from rhub_cli.models.rhub_api_tower_update_template_json_body import RhubApiTowerUpdateTemplateJsonBody

from .jobs import jobs
from .launch import launch


@click.group()
def template():
    pass


@template.command()
@click.option("--filter-name", type=str)
@click.option("--filter-server-id", type=int)
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@pass_api
def get_list(
    api: APIRequest,
    filter_name,
    filter_server_id,
    sort,
    page,
    limit,
):
    """Get list of Tower templates"""

    sort = RhubApiTowerListTemplatesSort(sort)

    filter_ = RhubApiTowerListTemplatesFilter(
        name=filter_name,
        server_id=filter_server_id,
    )

    response = template_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@template.command()
@click.option("--name", type=str)
@click.option("--server-id", type=int)
@click.option("--tower-template-id", type=int)
@click.option("--tower-template-is-workflow", is_flag=True)
@click.option("--description", type=str)
@pass_api
def create(
    api: APIRequest,
    name,
    server_id,
    tower_template_id,
    tower_template_is_workflow,
    description,
):
    """Create Tower template"""

    json_body = RhubApiTowerCreateTemplateJsonBody(
        name=name,
        server_id=server_id,
        tower_template_id=tower_template_id,
        tower_template_is_workflow=tower_template_is_workflow,
        description=description,
    )

    response = template_create(
        json_body=json_body,
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
@click.option("--credentials", type=str)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--name", type=str)
@click.option("--url", type=str)
@click.option("--verify-ssl", is_flag=True)
@pass_api
def update(
    api: APIRequest,
    template_id,
    credentials,
    description,
    enabled,
    name,
    url,
    verify_ssl,
):
    """Change Tower template"""

    json_body = RhubApiTowerUpdateTemplateJsonBody(
        credentials=credentials,
        description=description,
        enabled=enabled,
        name=name,
        url=url,
        verify_ssl=verify_ssl,
    )

    response = template_update(
        template_id=template_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


template.add_command(jobs)
template.add_command(launch)
