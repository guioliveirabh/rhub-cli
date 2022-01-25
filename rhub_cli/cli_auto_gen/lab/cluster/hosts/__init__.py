import click

from rhub_cli.api.lab.rhub_api_lab_cluster_create_cluster_hosts import sync_detailed as hosts_create
from rhub_cli.api.lab.rhub_api_lab_cluster_delete_cluster_hosts import sync_detailed as hosts_remove
from rhub_cli.api.lab.rhub_api_lab_cluster_list_cluster_hosts import sync_detailed as hosts_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models import *
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_hosts_json_body_item import (
    RhubApiLabClusterCreateClusterHostsJsonBodyItem,
)


@click.group()
def hosts():
    pass


@hosts.command()
@click.argument("cluster_id", type=int)
@pass_api
def get_list(
    api: APIRequest,
    cluster_id,
):
    """Get cluster hosts"""

    response = hosts_get_list(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@hosts.command()
@click.argument("cluster_id", type=int)
@click.option("--fqdn", type=str)
@click.option("--ipaddr", type=str, multiple=True)
@click.option("--num-vcpus", type=int)
@click.option("--num-volumes", type=int)
@click.option("--ram-mb", type=int)
@click.option("--volumes-gb", type=int)
@pass_api
def create(
    api: APIRequest,
    cluster_id,
    fqdn,
    ipaddr,
    num_vcpus,
    num_volumes,
    ram_mb,
    volumes_gb,
):
    """Create or update cluster hosts"""

    json_body_item = RhubApiLabClusterCreateClusterHostsJsonBodyItem(
        fqdn=fqdn,
        ipaddr=ipaddr,
        num_vcpus=num_vcpus,
        num_volumes=num_volumes,
        ram_mb=ram_mb,
        volumes_gb=volumes_gb,
    )

    response = hosts_create(
        cluster_id=cluster_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@hosts.command()
@click.argument("cluster_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    cluster_id,
):
    """Delete cluster hosts"""

    response = hosts_remove(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)
