import click

from rhub_cli.click.api_request import APIRequest, pass_api


@click.group(invoke_without_command=True)
@pass_api
@click.pass_context
def policies(context, api: APIRequest):
    """Handles policy API."""
    if context.invoked_subcommand is None:
        api.get('policies')


@policies.command()
@click.argument('policy_id', metavar='POLICY_ID', type=click.INT, required=False)
@pass_api
def get(api: APIRequest, policy_id):
    """Gets a policy details"""
    end_point = 'policies'
    if policy_id:
        end_point += f"/{policy_id}"
    api.get(end_point)


@policies.command()
@click.argument('policy_id', metavar='POLICY_ID', type=click.INT)
@pass_api
def remove(api: APIRequest, policy_id):
    """Removes a policy"""
    api.delete(f"policies/{policy_id}")


@policies.command()
@click.option('--name', required=True, help='Policy name.')
@click.option('--department', required=True, help='Policy department.')
@pass_api
def create(api: APIRequest, name, department):
    """Creates a policy"""
    api.post('policies', {'name': name, 'department': department})


@policies.command()
@click.argument('policy_id', metavar='POLICY_ID', type=click.INT)
@click.option('--name', help='Policy name.')
@click.option('--department', help='Policy department.')
@pass_api
def update(api: APIRequest, policy_id, name, department):
    """Updates a policy"""
    data = {}
    if name:
        data['name'] = name
    if department:
        data['department'] = department
    if not data:
        raise RuntimeError('Fill the fields')  # TODO

    api.patch(f"policies/{policy_id}", data)
