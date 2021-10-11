import click

from ...utils.config_manager import create_config, get_config_path


def manage(reset):
    if reset:
        click.secho("Resetting config file to default version", fg="cyan")
        create_config()
    else:
        click.secho(f"Config file is located at {get_config_path()}",
                    fg="cyan")
