import subprocess
import click
import sys
from pathlib import Path

from ...utils.file_manager import check_diff, is_file_empty, print_file
from ...utils.folder_manager import Task, delete_folder, clear_folder
from ..run.manager import is_interpreted, run_func, compile_source_code


def judge(
    task,
    base_folder,
    filename_without_extension,
    extension,
    gen_path,
    gen_extension,
    number_of_runs,
    config_data,
):
    clear_folder(task.last_run_folder)

    source_code_path = (base_folder / filename_without_extension).with_suffix(
        "." + extension
    )
    gen_folder = task.last_run_folder / "gen"
    gen_folder.mkdir()

    compilation_error_path = gen_folder / "compilation_error.txt"
    gen_compilation_error_path = gen_folder / "gen_compilation_error.txt"

    exec_path = Path()
    if not is_interpreted[extension]:
        exec_path = compile_source_code(
            source_code_path, compilation_error_path, extension, config_data
        )
    else:
        click.secho(f"Running the source code with command:", fg="cyan")
        click.secho(config_data["language"][extension]["command"] + "\n")

    gen_exec_path = Path()
    if not is_interpreted[gen_extension]:
        gen_exec_path = compile_source_code(
            gen_path, gen_compilation_error_path, gen_extension, config_data, True
        )
    else:
        click.secho(f"Running the generator code with command:", fg="cyan")
        click.secho(config_data["language"][gen_extension]["command"] + "\n")

    for current_run in range(number_of_runs):
        # gen input (empty file)
        gen_in_path = gen_folder / "gen_in.txt"
        gen_in_path.touch()

        # stdout of gen is same as the generated tc
        gen_std_output_path = gen_folder / "tc.txt"
        gen_std_error_path = gen_folder / "gen_error.txt"

        gen_run_returncode = 0
        if is_interpreted[gen_extension]:
            gen_run_returncode = run_func[gen_extension](
                gen_path,
                config_data["language"][gen_extension]["command"],
                gen_in_path,
                gen_std_output_path,
                gen_std_error_path,
            )
        else:
            gen_run_returncode = run_func[gen_extension](
                gen_exec_path, gen_in_path, gen_std_output_path, gen_std_error_path
            )

        if gen_run_returncode != 0:
            click.secho(f"Rumtime Error while generating testcase", fg="red")
            print_file(gen_std_error_path, 2)
            sys.exit(1)

        std_output_path = gen_folder / f"output.txt"
        std_error_path = gen_folder / f"error.txt"

        run_returncode = 0
        if is_interpreted[extension]:
            run_returncode = run_func[extension](
                source_code_path,
                config_data["language"][extension]["command"],
                gen_std_output_path,
                std_output_path,
                std_error_path,
            )
        else:
            run_returncode = run_func[extension](
                exec_path, gen_std_output_path, std_output_path, std_error_path
            )

        if run_returncode != 0:
            click.secho(f"Rumtime Error while running source code\n", fg="red")
            print_file(std_error_path, 2)
            click.secho(f"Testcase: ", fg="cyan")
            print_file(gen_std_output_path)
            sys.exit(0)

        if is_file_empty(std_output_path):
            click.secho(f"Accepted #{current_run + 1}\n", fg="green")

            if not is_file_empty(std_error_path):
                click.secho(f"Standard Error: ", fg="cyan")
                print_file(std_error_path)
        else:
            click.secho(f"Wrong Answer #{current_run + 1}\n", fg="red")

            click.secho(f"Test Case: ", fg="cyan")
            print_file(gen_std_output_path)

            click.secho(f"Standard Output: ", fg="cyan")
            print_file(std_output_path)

            if not is_file_empty(std_error_path):
                click.secho(f"Standard Error: ", fg="cyan")
                print_file(std_error_path)
            sys.exit(1)

    click.secho(f"Successfully passed {number_of_runs} testcases!", fg="green")


def manage(filename, number_of_runs, gen_path, base_folder, config_data):
    file_path = base_folder / filename
    extension = file_path.suffix[1:]

    gen_extension = gen_path.suffix[1:]

    filename_without_extension = file_path.stem
    if extension not in ["py", "java", "cpp"] or gen_extension not in [
        "py",
        "java",
        "cpp",
    ]:
        click.secho(
            f"Language {extension} is not supported (python(py), java, c++(cpp) are only supported)",
            err=True,
            fg="red",
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
            judge(
                task,
                base_folder,
                filename_without_extension,
                extension,
                gen_path,
                gen_extension,
                number_of_runs,
                config_data,
            )
