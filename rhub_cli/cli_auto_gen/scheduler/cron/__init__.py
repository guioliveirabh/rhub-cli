import click


@click.group()
def cron():
    pass


@cron.command()
def get_list():
    """Get CronJob list"""


@cron.command()
def create():
    """Create CronJob"""


@cron.command()
@click.argument("cron_job_id", type=int)
def get(
    cron_job_id,
):
    """Get CronJob"""


@cron.command()
@click.argument("cron_job_id", type=int)
def remove(
    cron_job_id,
):
    """Delete CronJob"""


@cron.command()
@click.argument("cron_job_id", type=int)
def update(
    cron_job_id,
):
    """Update CronJob"""
