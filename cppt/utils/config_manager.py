import sys
from pathlib import Path
from re import template

import click
import yaml

user_config_path = Path.home() / ".config/cppt/config.yaml"


def create_config():
    default_config_path = Path(__file__).parent / "default_config.yaml"
    user_config_path.parent.mkdir(parents=True, exist_ok=True)
    user_config_path.write_bytes(default_config_path.read_bytes())


def get_config_path():
    return user_config_path.resolve()


def check_config_data(data):
    is_invalid = False
    if "default_base_folder" in data:
        data["default_base_folder"] = data["default_base_folder"].replace(
            "~", str(Path.home()))
        default_base_folder_path = Path(data["default_base_folder"])
        default_base_folder_path.expanduser()
        if not default_base_folder_path.exists():
            click.secho(
                f"The default base folder ({default_base_folder_path.resolve()}) specified in config file does not exist",
                err=True,
                fg="red")
            is_invalid = True
        if not default_base_folder_path.is_dir():
            click.secho(
                f"The default base folder ({default_base_folder_path.resolve()}) specified in config file is not a directory",
                err=True,
                fg="red")
            is_invalid = True
    else:
        click.secho("The default base folder was not found in config",
                    err=True,
                    fg="red")
        is_invalid = True

    if "default_language" in data:
        if data["default_language"] not in ["cpp", "py", "java"]:
            click.secho(f"Invalid default language {data['default_language']}",
                        err=True,
                        fg="red")
            click.secho("python(py), java, c++(cpp) are only supported",
                        err=True,
                        fg="red")
            is_invalid = True
    else:
        click.secho("The default language was not defined in config",
                    err=True,
                    fg="red")
        is_invalid = True

    for lang in data["language"]:
        if data["language"][lang]["template"] is not None:
            data["language"][lang]["template"] = data["language"][lang][
                "template"].replace("~", str(Path.home()))
            template_path = Path(data["language"][lang]["template"])
            if not template_path.exists():
                click.secho(
                    f"template for {lang} ({template_path.resolve()}) specified in config file does not exist",
                    err=True,
                    fg="red")
                is_invalid = True
            elif template_path.is_dir():
                click.secho(
                    f"{template_path.resolve()} is a directory, should be a file",
                    err=True,
                    fg="red")
                is_invalid = True
            elif template_path.suffix[1:] != lang:
                click.secho(
                    f"file extension of template ({template_path.resolve()}) doesnot match with {lang}",
                    err=True,
                    fg="red")
                is_invalid = True

    if is_invalid:
        sys.exit(1)


def check_config():
    if not user_config_path.exists():
        click.secho(f"config not found at {user_config_path.resolve()}",
                    err=True,
                    fg="red")
        click.secho(f"creating config at {user_config_path.resolve()}",
                    fg="cyan")
        create_config()


def get_config_data():
    check_config()
    user_config_file = open(user_config_path, "r")
    user_config = yaml.safe_load(user_config_file)
    check_config_data(user_config)
    return user_config


if __name__ == "__main__":
    get_config_data()
