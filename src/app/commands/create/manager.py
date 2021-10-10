import sys
from pathlib import Path

import click

from ...internal.folder_manager import Task


def manage(filename, base_folder, force):
    file_path = base_folder / filename
    extension = file_path.suffix
    filename_without_extension = file_path.stem
    if extension not in [".py", ".java", ".cpp"]:
        click.secho(
            f"Language {file_path.suffix} is not supported (.py, .java, .cpp are only supported)",
            err=True,
            fg="red")
        sys.exit(1)
    else:
        task = Task(base_folder, filename_without_extension, extension)
        task_status = task.task_exists()
        if task_status != 0:
            if not force:
                if task_status == 1:
                    click.secho("Source code already exists",
                                err=True,
                                fg="red")
                elif task_status == 2:
                    click.secho("Test data already exists", err=True, fg="red")
                else:
                    click.secho(
                        "Both source code and test data already exists",
                        err=True,
                        fg="red")

                click.secho(
                    "To overwrite existing files specify --force option",
                    err=True,
                    fg="red")
                sys.exit(1)
            else:
                task.overwrite()
        task.create_task()
        click.secho("Successfully created task", fg="green")
