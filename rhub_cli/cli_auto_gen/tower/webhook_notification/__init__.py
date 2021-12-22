import click

from rhub_cli.api.tower.rhubapitowerwebhook_notification import sync_detailed as webhook_notification_create
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhubapitowerwebhook_notification_json_body import RhubapitowerwebhookNotificationJsonBody


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
):
    """Incoming webhook notification from Tower"""

    json_body = RhubapitowerwebhookNotificationJsonBody(
        body=body,
        created_by=created_by,
        credential=credential,
        extra_vars=extra_vars,
        finished=finished,
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
