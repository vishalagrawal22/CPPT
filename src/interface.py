from pathlib import Path

import click

from .app import *


@click.group()
def cli():
    pass


@cli.command()
@click.argument("filename", type=str)
@click.option("-p",
              "--path",
              "base_folder",
              show_default=True,
              default=Path("."),
              type=click.Path(exists=True, path_type=Path, writable=True))
@click.option("--force", is_flag=True)
def create(filename, base_folder, force):
    create_manage(filename, base_folder, force)


@cli.command()
@click.option("-p",
              "--path",
              "base_folder",
              show_default=True,
              default=Path("."),
              type=click.Path(exists=True, path_type=Path, writable=True))
@click.option("--force", is_flag=True)
def fetch(base_folder, force):
    fetch_manage(base_folder, force)


@cli.command()
@click.argument("filename", type=str)
@click.option("-p",
              "--path",
              "base_folder",
              show_default=True,
              default=Path("."),
              type=click.Path(exists=True, path_type=Path, writable=True))
def run(filename, base_folder):
    run_manage(filename, base_folder)


@cli.command()
@click.option("--reset", "-r", is_flag=True)
def config(reset):
    config_manage(reset)
