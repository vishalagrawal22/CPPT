import click
import sys

from ....utils.folder_manager import (
    exit_if_invalid_extension,
    exit_if_invalid_task,
    Task,
)


def manage(filename, base_folder, editor):
    file_path = base_folder / filename
    extension = file_path.suffix[1:]
    filename_without_extension = file_path.stem

    exit_if_invalid_extension(extension)

    task = Task(base_folder, filename_without_extension, extension)

    exit_if_invalid_task(task)

    try:
        testcase = {}

        click.secho("Waiting for input file to close", fg="cyan")
        testcase["input"] = click.edit(
            "Enter the input and save the file (delete the help text before saving).\nYou can set the input editor in config file (the default editor is vim, use :q to exit if you opened it by mistake)",
            editor=editor,
        )
        if testcase["input"] is None:
            click.secho("Input file closed without saving\n", fg="red", err=True)
            sys.exit(1)

        click.secho(testcase["input"] + "\n")

        click.secho("Waiting for output file to close", fg="cyan")
        testcase["output"] = click.edit(
            "Enter the output and save the file (delete the help text before saving).\nYou can set the input editor in config file (the default editor is vim, use :q to exit if you opened it by mistake)",
            editor=editor,
        )
        if testcase["output"] is None:
            click.secho("Output file closed without saving\n", fg="red", err=True)
            sys.exit(1)

        click.secho(testcase["output"] + "\n")

        task.add_test(testcase)
        click.secho("Created testcase file", fg="green")
    except click.UsageError:
        click.secho(
            "Unable to open editor for testcase input (check config file for potential errors).\n",
            fg="red",
            err=True,
        )
        sys.exit(1)
