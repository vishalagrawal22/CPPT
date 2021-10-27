import re
import sys
from pathlib import Path

import click


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


def print_file(file_path, is_error=False):
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
            click.secho(line, fg="red", err=is_error, nl=False)
    click.echo("")