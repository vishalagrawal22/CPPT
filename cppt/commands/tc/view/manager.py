import click

from ....utils.folder_manager import (
    exit_if_invalid_extension,
    exit_if_invalid_task,
    Task,
)


def manage(filename, base_folder, tcs):
    file_path = base_folder / filename
    extension = file_path.suffix[1:]
    filename_without_extension = file_path.stem

    exit_if_invalid_extension(extension)

    task = Task(base_folder, filename_without_extension, extension)

    exit_if_invalid_task(task)

    if tcs[0] == 0:
        tcs = task.get_tc_list()

    if len(tcs) == 0:
        click.secho("No testcases found!", fg="cyan")
    else:
        tcs_data = task.get_tcs(tcs)
        for index, tc_data in enumerate(tcs_data):
            if tc_data is None:
                click.secho(f"TC #{tcs[index]} does not exist\n", fg="red")
            else:
                click.secho(f"Input #{tcs[index]}:", fg="cyan")
                click.secho(tc_data["input"] + "\n")

                click.secho(f"Output #{tcs[index]}: ", fg="cyan")
                click.secho(tc_data["output"] + "\n")
