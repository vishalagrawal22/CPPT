import sys
from pathlib import Path

import click

from ...internal.file_manager import read_from_file
from ...internal.folder_manager import Task


def manage(filename, input, output, base_folder):
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
        task_status = task.task_exists()
        if task_status != 3:
            if task_status == 0:
                click.secho(
                    f"Neither source code nor task folder exists at {task.source_code.resolve()} and {task.task_folder.resolve()} respectively",
                    err=True,
                    fg="red")
            elif task_status == 1:
                click.secho(
                    f"Task folder does not exist at {task.task_folder.resolve()}",
                    err=True,
                    fg="red")
            elif task_status == 2:
                click.secho(
                    f"Source code does not exist at {task.source_code.resolve()}",
                    err=True,
                    fg="red")

            click.secho(
                "Try overwriting existing files with create or fetch commands's --force option",
                err=True,
                fg="red")
            click.secho(
                "Caution: do not forget to copy any code in source file before using --force option",
                err=True,
                fg="red")
            sys.exit(1)
        input_path = base_folder / input
        output_path = base_folder / output
        if not input_path.exists():
            click.secho(
                f"Test input file doesnot exist at {input_path.resolve()}",
                err=True,
                fg="red")
            sys.exit(1)
        if not input_path.is_file():
            click.secho(
                f"Test input should be a file ({input_path.resolve()} is not a file)",
                err=True,
                fg="red")
            sys.exit(1)
        if not output_path.exists():
            click.secho(
                f"Test output file doesnot exist at {output_path.resolve()}",
                err=True,
                fg="red")
            sys.exit(1)
        if not output_path.is_file():
            click.secho(
                f"Test output should be a file ({output_path.resolve()} is not a file)",
                err=True,
                fg="red")
            sys.exit(1)

        tc_list = task.get_tc_list()
        tc_no = 1
        if tc_list != []:
            tc_no = tc_list[-1] + 1
        test = [{
            "input": read_from_file(input_path),
            "output": read_from_file(output_path)
        }]
        task.add_tests(test, tc_no)
        click.secho(f"Added testcase successfully", fg="green")
