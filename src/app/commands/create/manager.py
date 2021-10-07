import sys
import click
from pathlib import Path

from ...internal.folder_manager import Task

def manage(filename, base_folder, force):
    file_path = base_folder / filename
    extension = file_path.suffix
    filename_without_extension = file_path.stem
    if extension not in [".py", ".java", ".cpp"]:
        click.secho(f"language {file_path.suffix} is not supported (.py, .java, .cpp are only supported)", err=True, fg="red")
        sys.exit(1)
    else:
        task = Task(base_folder, filename_without_extension, extension)
        if task.task_exists():
            if not force:
                click.secho("Source code or test data exist with the same name", err=True, fg="red")
                click.secho("To overwrite them specify --force option", err=True, fg="red")
                sys.exit(1) 
            else:
                task.overwrite()
        task.create_task()
        click.secho("Successfully created task", fg="green")