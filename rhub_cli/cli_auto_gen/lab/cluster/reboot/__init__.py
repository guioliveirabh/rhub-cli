import click

from rhub_cli.api.lab.rhubapilabclusterreboot_hosts import sync_detailed as reboot_create
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapilabclusterreboot_hosts_json_body import RhubapilabclusterrebootHostsJsonBody


@click.group()
def reboot():
    pass


@reboot.command()
@click.argument("cluster_id", type=int)
@click.option("--hosts")
@click.option("--type")
@pass_api
def create(
    api: APIRequest,
    cluster_id,
    hosts,
    type,
):
    """Reboot cluster hosts"""

    json_body = RhubapilabclusterrebootHostsJsonBody(
        hosts=hosts,
        type=type,
    )

    response = reboot_create(
        cluster_id=cluster_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
