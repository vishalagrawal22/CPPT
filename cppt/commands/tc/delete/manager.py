import click

from ....utils.folder_manager import (
    exit_if_invalid_extension,
    exit_if_invalid_task,
    Task,
)


def manage(filename, base_folder, delete_tc_nos):
    file_path = base_folder / filename
    extension = file_path.suffix[1:]
    filename_without_extension = file_path.stem

    exit_if_invalid_extension(extension)

    task = Task(base_folder, filename_without_extension, extension)

    exit_if_invalid_task(task)

    if delete_tc_nos[0] == 0:
        delete_tc_nos = task.get_tc_list()

    if len(delete_tc_nos) == 0:
        click.secho("No testcases found!", fg="cyan")
    else:
        tc_nos = task.get_tc_list()
        tc_data = task.get_tcs(tc_nos)
        task.clear_tcs()

        delete_tc_nos = sorted(delete_tc_nos, reverse=True)
        for delete_tc_no in delete_tc_nos:
            if delete_tc_no not in tc_nos:
                click.secho(f"TC #{delete_tc_no} does not exist\n", fg="red")
            else:
                del tc_data[delete_tc_no - 1]

        task.add_tests(tc_data)
        click.secho("Deleted testcase files", fg="green")
