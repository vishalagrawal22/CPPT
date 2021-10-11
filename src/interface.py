from pathlib import Path

import click

from .app import *


@click.group()
def cli():
    global config_data
    config_data = get_config_data()


@cli.command()
@click.argument("filename", type=str)
@click.option("-p",
              "--path",
              "base_folder",
              default=None,
              type=click.Path(exists=True, path_type=Path, writable=True))
@click.option("--force", is_flag=True)
def create(filename, base_folder, force):
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])
    create_manage(filename, base_folder, force, config_data)


@cli.command()
@click.option("-p",
              "--path",
              "base_folder",
              default=None,
              type=click.Path(exists=True, path_type=Path, writable=True))
@click.option("--force", is_flag=True)
def fetch(base_folder, force):
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])
    fetch_manage(base_folder, force, config_data)


@cli.command()
@click.argument("filename", type=str)
@click.option("-p",
              "--path",
              "base_folder",
              default=None,
              type=click.Path(exists=True, path_type=Path, writable=True))
def run(filename, base_folder):
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])
    run_manage(filename, base_folder, config_data)


@cli.command()
@click.option("--reset", "-r", is_flag=True)
def config(reset):
    config_manage(reset)
