import click

from ....utils.folder_manager import (
    exit_if_invalid_extension,
    exit_if_invalid_task,
    Task,
)


def manage(filename, base_folder, test):
    file_path = base_folder / filename
    extension = file_path.suffix[1:]
    filename_without_extension = file_path.stem

    exit_if_invalid_extension(extension)

    task = Task(base_folder, filename_without_extension, extension)

    exit_if_invalid_task(task)

    task.add_test(test)
    click.secho("Created testcase file", fg="green")
