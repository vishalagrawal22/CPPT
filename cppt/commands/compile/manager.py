import sys

import click

from ...utils.folder_manager import Task
from ..run.manager import compile_source_code, is_interpreted


def manage(filename, base_folder, config_data):
    source_code_path = base_folder / filename
    extension = source_code_path.suffix[1:]
    filename_without_extension = source_code_path.stem
    if extension not in ["py", "java", "cpp"]:
        click.secho(
            f"Language {extension} is not supported (python(py), java, c++(cpp) are only supported)",
            err=True,
            fg="red",
        )
        sys.exit(1)
    elif is_interpreted[extension]:
        click.secho(
            f"Language {extension} does not support compilation", err=True, fg="red"
        )
        sys.exit(1)
    else:
        task = Task(base_folder, filename_without_extension, extension)
        task_status = task.task_exists()
        if task_status not in [1, 3]:
            click.secho("Source Code does not exist", err=True, fg="red")
            sys.exit(1)
        else:
            if task_status == 1:
                task.create_task(create_source_code=False)
            compilation_error_path = task.last_run_folder / "compilation_error.txt"
            compile_source_code(
                source_code_path, compilation_error_path, extension, config_data
            )
