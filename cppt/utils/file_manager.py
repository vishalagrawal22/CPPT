import re
import subprocess
import sys
from pathlib import Path

import click

from .config_manager import get_config_path


# checks if file is empty (only contains white spaces)
def is_file_empty(file_path):
    content = open(file_path, 'r').read()
    if re.search(r'^\s*$', content):
        return True
    return False


def check_diff(file_path1, file_path2):
    file1_txt = (read_from_file(file_path1)).split()
    file2_txt = (read_from_file(file_path2)).split()
    if len(file1_txt) != len(file2_txt):
        return False
    for i in range(len(file1_txt)):
        if file1_txt[i] != file2_txt[i]:
            return False
    return True


def write_to_file(file_path, text):
    with open(file_path, "w") as file:
        file.write(text)


def read_from_file(file_path):
    file = open(file_path, "r")
    text = "".join(file.readlines())
    file.close()
    return text


def print_file(file_path, is_error=0):
    """
        is_error = 0 -> normal text
        is_error = 1 -> warning text
        is_error = 2 -> error text
    """
    if not file_path.exists():
        click.secho(f"File at {file_path.resolve()} does not exist",
                    fg="red",
                    err=True)
        sys.exit(1)
    elif not file_path.is_file():
        click.secho(f"{file_path.resolve()} is not a file", fg="red", err=True)
        sys.exit(1)

    with open(file_path, 'r') as file:
        for line in file.readlines():
            if is_error == 2:
                click.secho(line, fg="red", err=True, nl=False)
            elif is_error == 1:
                click.secho(line, fg="yellow", err=True, nl=False)
            elif is_error == 0:
                click.secho(line, nl=False)
    click.echo("")


def open_source_code_in_editor(config_data, file_path):
    if "editor" in config_data:
        if config_data["editor"] is not None:
            click.secho(
                f"Opening {file_path.resolve()} with {config_data['editor']}",
                fg="cyan")
            try:
                subprocess.run([config_data['editor'], file_path])
            except OSError:
                click.secho(f"Command not found: {config_data['editor']}",
                            fg="red")
                click.secho(
                    f"Try changing the command in the config file (located at {get_config_path()})",
                    fg="cyan")
                sys.exit(1)
