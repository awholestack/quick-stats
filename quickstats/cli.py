import click
import psutil
from quickstats.util import bytes_to_human


@click.group()
def cli():
    pass


@click.command(name="memory", help="Show memory stats")
@click.option("--total", default=False, is_flag=True, help="show total memory")
@click.option("--available", default=False, is_flag=True, help="show available memory")
@click.option("--all", default=False, is_flag=True, help="show all stats")
def memory(total, available, all):
    if available or all:
        avail_ram = psutil.virtual_memory().available
        avail_ram_human = bytes_to_human(avail_ram)
        click.echo("Available RAM: {}".format(avail_ram_human))
    if total or all:
        total_ram = psutil.virtual_memory().total
        total_ram_human = bytes_to_human(total_ram)
        click.echo("Total RAM: {}".format(total_ram_human))


cli.add_command(memory)
