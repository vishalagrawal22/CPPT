import sys
from pathlib import Path

import click

from ...utils.file_manager import open_source_code_in_editor
from ...utils.folder_manager import Task


def manage(filename, base_folder, force, config_data):
    file_path = base_folder / filename
    extension = file_path.suffix[1:]
    filename_without_extension = file_path.stem
    if extension not in ["py", "java", "cpp"]:
        click.secho(
            f"Language {extension} is not supported (python(py), java, c++(cpp) are only supported)",
            err=True,
            fg="red")
        sys.exit(1)
    else:
        task = Task(base_folder, filename_without_extension, extension)
        task.safe_overwrite(force)
        task.create_task(
            template_path=config_data["language"][extension]["template"])
        click.secho(f"Successfully created task", fg="green")
        click.secho(f"Source code is located at {task.source_code.resolve()}",
                    fg="green")
        open_source_code_in_editor(config_data, task.source_code)
