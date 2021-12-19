import click

from rhub_cli.api.tower.rhubapitowerwebhook_notification import sync_detailed as webhook_notification_create
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def webhook_notification():
    pass


@webhook_notification.command()
@pass_api
def create(
    api: APIRequest,
):
    """Incoming webhook notification from Tower"""
    # TODO: json_body

    response = webhook_notification_create(
        client=api.authenticated_client,
    )
    api.handle_response(response)
