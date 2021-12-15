import click

from .cluster import cluster
from .cluster_event import cluster_event
from .product import product
from .region import region


@click.group()
def lab():
    pass


lab.add_command(cluster)
lab.add_command(cluster_event)
lab.add_command(product)
lab.add_command(region)
