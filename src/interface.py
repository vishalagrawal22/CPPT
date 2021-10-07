import click
from pathlib import Path

from .app import *


@click.group()
def cli():
    pass


@cli.command()
@click.argument("filename", type=str)
@click.option("-p", "--path", "base_folder", show_default=True, default=Path("."), type=click.Path(exists=True, path_type=Path, writable=True))
@click.option("--force", is_flag=True)
def create(filename, base_folder, force):
    create_manage(filename, base_folder, force)


@cli.command()
@click.option("-p", "--path", "base_folder", show_default=True, default=Path("."), type=click.Path(exists=True, path_type=Path, writable=True))
@click.option("--force", is_flag=True)
def fetch(base_folder, force):
    fetch_manage(base_folder, force)
