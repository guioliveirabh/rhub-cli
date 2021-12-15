import click

from .auth import auth
from .cowsay import cowsay
from .lab import lab
from .me import me
from .ping import ping
from .policies import policies
from .scheduler import scheduler
from .tower import tower


@click.group()
def cli_auto_gen():
    pass


cli_auto_gen.add_command(auth)
cli_auto_gen.add_command(cowsay)
cli_auto_gen.add_command(lab)
cli_auto_gen.add_command(me)
cli_auto_gen.add_command(ping)
cli_auto_gen.add_command(policies)
cli_auto_gen.add_command(scheduler)
cli_auto_gen.add_command(tower)
