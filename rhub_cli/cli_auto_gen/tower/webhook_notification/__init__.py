import click

from rhub_cli.api.tower.rhub_api_tower_webhook_notification import sync_detailed as webhook_notification_create
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_tower_webhook_notification_json_body import RhubApiTowerWebhookNotificationJsonBody
from rhub_cli.models.rhub_api_tower_webhook_notification_json_body_hosts import (
    RhubApiTowerWebhookNotificationJsonBodyHosts,
)
from rhub_cli.models.rhub_api_tower_webhook_notification_json_body_hosts_additional_property import (
    RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalProperty,
)
from rhub_cli.models.rhub_api_tower_webhook_notification_json_body_hosts_additional_property_localhost import (
    RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost,
)


@click.group()
def webhook_notification():
    pass


@webhook_notification.command()
@click.option("--body", type=str)
@click.option("--created-by", type=str)
@click.option("--credential", type=str)
@click.option("--extra-vars", type=str)
@click.option("--finished", type=click.DateTime())
@click.option("--id", type=int)
@click.option("--inventory", type=str)
@click.option("--limit", type=str)
@click.option("--name", type=str)
@click.option("--playbook", type=str)
@click.option("--project", type=str)
@click.option("--started", type=click.DateTime())
@click.option("--status", type=str)
@click.option("--traceback", type=str)
@click.option("--url", type=str)
@click.option("--hosts-additional-property-localhost-changed", type=int)
@click.option("--hosts-additional-property-localhost-dark", type=int)
@click.option("--hosts-additional-property-localhost-failed", is_flag=True)
@click.option("--hosts-additional-property-localhost-failures", type=int)
@click.option("--hosts-additional-property-localhost-ignored", type=int)
@click.option("--hosts-additional-property-localhost-ok", type=int)
@click.option("--hosts-additional-property-localhost-processed", type=int)
@click.option("--hosts-additional-property-localhost-rescued", type=int)
@click.option("--hosts-additional-property-localhost-skipped", type=int)
@pass_api
def create(
    api: APIRequest,
    body,
    created_by,
    credential,
    extra_vars,
    finished,
    id,
    inventory,
    limit,
    name,
    playbook,
    project,
    started,
    status,
    traceback,
    url,
    hosts_additional_property_localhost_changed,
    hosts_additional_property_localhost_dark,
    hosts_additional_property_localhost_failed,
    hosts_additional_property_localhost_failures,
    hosts_additional_property_localhost_ignored,
    hosts_additional_property_localhost_ok,
    hosts_additional_property_localhost_processed,
    hosts_additional_property_localhost_rescued,
    hosts_additional_property_localhost_skipped,
):
    """Incoming webhook notification from Tower"""

    hosts_additional_property_localhost = RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost(
        changed=hosts_additional_property_localhost_changed,
        dark=hosts_additional_property_localhost_dark,
        failed=hosts_additional_property_localhost_failed,
        failures=hosts_additional_property_localhost_failures,
        ignored=hosts_additional_property_localhost_ignored,
        ok=hosts_additional_property_localhost_ok,
        processed=hosts_additional_property_localhost_processed,
        rescued=hosts_additional_property_localhost_rescued,
        skipped=hosts_additional_property_localhost_skipped,
    )

    hosts_additional_property = RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalProperty(
        localhost=hosts_additional_property_localhost,
    )

    hosts = RhubApiTowerWebhookNotificationJsonBodyHosts()
    hosts.additional_properties = {"hosts": hosts_additional_property}

    json_body = RhubApiTowerWebhookNotificationJsonBody(
        body=body,
        created_by=created_by,
        credential=credential,
        extra_vars=extra_vars,
        finished=finished,
        hosts=hosts,
        id=id,
        inventory=inventory,
        limit=limit,
        name=name,
        playbook=playbook,
        project=project,
        started=started,
        status=status,
        traceback=traceback,
        url=url,
    )

    response = webhook_notification_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)
