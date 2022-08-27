import click
import sys

from ....utils.folder_manager import (
    exit_if_invalid_extension,
    exit_if_invalid_task,
    Task,
)


def manage(filename, base_folder, tc_nos, editor):
    file_path = base_folder / filename
    extension = file_path.suffix[1:]
    filename_without_extension = file_path.stem

    exit_if_invalid_extension(extension)

    task = Task(base_folder, filename_without_extension, extension)

    exit_if_invalid_task(task)

    if tc_nos[0] == 0:
        tc_nos = task.get_tc_list()

    if len(tc_nos) == 0:
        click.secho("No testcases found!", fg="cyan")
    else:
        testcases = []
        tcs_data = task.get_tcs(tc_nos)
        for tc_number, tc_data in zip(tc_nos, tcs_data):
            if tc_data is None:
                click.secho(f"TC #{tc_number} does not exist\n", fg="red")
            else:
                try:
                    testcase = {}
                    click.secho(f"Input #{tc_number}", fg="cyan")
                    testcase["input"] = click.edit(
                        tc_data["input"],
                        editor=editor,
                    )

                    if testcase["input"] is None:
                        click.secho(
                            "Input file closed without saving\n", fg="red", err=True
                        )
                        sys.exit(1)

                    click.secho(testcase["input"] + "\n")

                    click.secho(f"Output #{tc_number}", fg="cyan")
                    testcase["output"] = click.edit(
                        tc_data["output"],
                        editor=editor,
                    )
                    if testcase["output"] is None:
                        click.secho(
                            "Output file closed without saving\n", fg="red", err=True
                        )
                        sys.exit(1)

                    click.secho(testcase["output"] + "\n")

                    testcases.append(testcase)

                except click.UsageError:
                    click.secho(
                        "Unable to open editor for testcase input (check config file for potential errors).\n",
                        fg="red",
                        err=True,
                    )
                    sys.exit(1)

        task.edit_tcs(tc_nos, testcases)
        click.secho("Edited testcase files", fg="green")
