import sys
from pathlib import Path

import click

from ...internal.folder_manager import Task
from .server import get_task_data


def get_file_name(task_name):
    name_char_list = []
    last_was_alnum = 0
    for ch in task_name:
        if ch.isalnum():
            name_char_list.append(ch)
            last_was_alnum = 1
        else:
            if last_was_alnum:
                name_char_list.append('_')
            last_was_alnum = 0
    return "".join(name_char_list)


def get_default_language():
    return ".cpp"


def manage(base_folder, force):
    task_data = get_task_data()
    tests = task_data["tests"]
    filename_without_extension = get_file_name(task_data["name"])
    extension = get_default_language()

    task = Task(base_folder, filename_without_extension, extension)
    if task.task_exists():
        if not force:
            click.secho("Source code or test data exist with the same name",
                        err=True,
                        fg="red")
            click.secho("To overwrite them specify --force option",
                        err=True,
                        fg="red")
            sys.exit(1)
        else:
            task.overwrite()
    task.create_task(tests)
    click.secho("Successfully created task", fg="green")
