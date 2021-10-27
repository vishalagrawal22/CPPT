import sys
from pathlib import Path

import click

from ...utils.file_manager import open_source_code_in_editor
from ...utils.folder_manager import Task
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


def manage(base_folder, force, config_data):
    task_data = get_task_data()
    tests = task_data["tests"]
    filename_without_extension = get_file_name(task_data["name"])
    extension = config_data["default_language"]

    task = Task(base_folder, filename_without_extension, extension)
    task.safe_overwrite(force)
    task.create_task(tests, config_data["language"][extension]["template"])
    click.secho(f"Successfully created task", fg="green")
    click.secho(f"Source code is located at {task.source_code.resolve()}",
                fg="green")
    open_source_code_in_editor(config_data, task.source_code)
