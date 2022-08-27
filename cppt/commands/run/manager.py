import re
import subprocess
import sys
from pathlib import Path

import click

from ...utils.config_manager import get_config_path
from ...utils.file_manager import (
    check_diff,
    is_file_empty,
    print_file,
    read_from_file,
    write_to_file,
)
from ...utils.folder_manager import Task, clear_folder


def cpp_compile(source_code_path, error_path, command):
    file_name_without_extension = source_code_path.stem
    exec_path = source_code_path.parent / file_name_without_extension
    command = command.split()
    command.extend([source_code_path, "-o", exec_path])
    try:
        compilation_data = subprocess.run(command, capture_output=True, text=True)
    except OSError:
        click.secho(
            f"Command not found: {' '.join(map(str, command))}", fg="red", err=True
        )
        click.secho(
            f"Try changing the command in the config file (located at {get_config_path()})",
            fg="cyan",
        )
        sys.exit(1)

    write_to_file(error_path, compilation_data.stderr)
    return [exec_path, compilation_data.returncode]


def cpp_run(
    exec_path, input_path=None, output_path=None, error_path=None, interactive=False
):
    if not interactive:
        try:
            run_data = subprocess.run(
                [exec_path.resolve()],
                input=read_from_file(input_path),
                capture_output=True,
                text=True,
            )
        except Exception as e:
            click.secho(
                f"Unknown Error while running {exec_path.resolve()}", fg="red", err=True
            )
            sys.exit(1)
        write_to_file(error_path, run_data.stderr)
        write_to_file(output_path, run_data.stdout)
        return run_data.returncode
    else:
        subprocess.run([exec_path.resolve()])


def java_compile(source_code_path, error_path, command):
    file_name_without_extension = source_code_path.stem
    exec_path = source_code_path.parent / file_name_without_extension
    command = command.split()
    command.extend([source_code_path])
    try:
        compilation_data = subprocess.run(command, capture_output=True, text=True)
    except OSError:
        click.secho(
            f"Command not found: {' '.join(map(str, command))}", fg="red", err=True
        )
        click.secho(
            f"Try changing the command in the config file (located at {get_config_path()})",
            fg="cyan",
        )
        sys.exit(1)
    write_to_file(error_path, compilation_data.stderr)

    return [exec_path, compilation_data.returncode]


def java_run(
    exec_path, input_path=None, output_path=None, error_path=None, interactive=False
):
    if not interactive:
        try:
            run_data = subprocess.run(
                ["java", exec_path],
                input=read_from_file(input_path),
                capture_output=True,
                text=True,
            )
        except Exception as e:
            click.secho(
                f"Unknown Error while running {'java' + str(exec_path.resolve())}",
                fg="red",
                err=True,
            )
            sys.exit(1)
        write_to_file(error_path, run_data.stderr)
        write_to_file(output_path, run_data.stdout)
        return run_data.returncode
    else:
        subprocess.run(["java", exec_path])


# exec path incase of interpreted language is source code path
def py_run(
    source_code_path,
    command,
    input_path=None,
    output_path=None,
    error_path=None,
    interactive=False,
):
    command = command.split()
    command.extend([source_code_path])
    if not interactive:
        try:
            run_data = subprocess.run(
                command,
                input=read_from_file(input_path),
                capture_output=True,
                text=True,
            )
        except OSError:
            click.secho(
                f"Command not found: {' '.join(map(str, command))}", fg="red", err=True
            )
            click.secho(
                f"Try changing the command in the config file (located at {get_config_path()})",
                fg="cyan",
            )
            sys.exit(1)
        except Exception as e:
            click.secho(
                f"Unknown Error while running {' '.join(map(str, command))}",
                fg="red",
                err=True,
            )
            sys.exit(1)
        write_to_file(error_path, run_data.stderr)
        write_to_file(output_path, run_data.stdout)
        return run_data.returncode
    else:
        subprocess.run(command)


is_interpreted = {
    "py": True,
    "java": False,
    "cpp": False,
}

run_func = {
    "py": py_run,
    "java": java_run,
    "cpp": cpp_run,
}

compile_func = {
    "java": java_compile,
    "cpp": cpp_compile,
}


def compile_source_code(
    source_code_path, compilation_error_path, extension, config_data, gen_compile=False
):
    if not gen_compile:
        click.secho(f"Compiling the source code with command:", fg="cyan")
    else:
        click.secho(f"Compiling the generator code with command:", fg="cyan")
    click.secho(config_data["language"][extension]["command"] + "\n")
    exec_path, compile_returncode = compile_func[extension](
        source_code_path,
        compilation_error_path,
        config_data["language"][extension]["command"],
    )
    if compile_returncode != 0:
        click.secho(f"Compilation Error:\n", fg="red")
        print_file(compilation_error_path, 2)
        sys.exit()
    else:
        click.secho(f"Compiled Successfully\n", fg="green")
        if not is_file_empty(compilation_error_path):
            click.secho(f"Compilation Warning:\n", fg="cyan")
            print_file(compilation_error_path, 1)
    return exec_path


def judge(
    task,
    filename_without_extension,
    extension,
    base_folder,
    config_data,
    tc,
    interactive,
):
    clear_folder(task.last_run_folder)

    source_code_path = (base_folder / filename_without_extension).with_suffix(
        "." + extension
    )
    compilation_error_path = task.last_run_folder / "compilation_error.txt"

    exec_path = Path()
    if not is_interpreted[extension]:
        exec_path = compile_source_code(
            source_code_path, compilation_error_path, extension, config_data
        )
    else:
        click.secho(f"Running the source code with command:", fg="cyan")
        click.secho(config_data["language"][extension]["command"] + "\n")

    if not interactive:
        tc_list = []
        if tc == 0:
            tc_list = task.get_tc_list()
        else:
            tc_list.append(tc)

        if tc_list == []:
            click.secho(f"No testcase to run!", fg="red")
            sys.exit(1)

        for num in tc_list:
            in_path = task.tc_folder / f"in{num}.txt"
            ans_path = task.tc_folder / f"ans{num}.txt"
            if not in_path.is_file() and not ans_path.is_file():
                click.secho(f"Skipped #{num}\n", fg="yellow")
                click.secho(
                    f"Input file and Answer file both are not present\n",
                    fg="red",
                    err=True,
                )
                continue
            elif not in_path.is_file():
                click.secho(f"Skipped #{num}\n", fg="yellow")
                click.secho(f"Input file is not present\n", fg="red", err=True)
                continue
            elif not ans_path.is_file():
                click.secho(f"Skipped #{num}\n", fg="yellow")
                click.secho(f"Answer file is not present\n", fg="red", err=True)
                continue
            std_output_path = task.last_run_folder / f"output{num}.txt"
            std_error_path = task.last_run_folder / f"error{num}.txt"

            click.secho(f"Running TC #{num}\n", fg="cyan")

            run_returncode = 0
            if is_interpreted[extension]:
                run_returncode = run_func[extension](
                    source_code_path,
                    config_data["language"][extension]["command"],
                    in_path,
                    std_output_path,
                    std_error_path,
                )
            else:
                run_returncode = run_func[extension](
                    exec_path, in_path, std_output_path, std_error_path
                )

            if run_returncode != 0:
                click.secho(f"Rumtime Error #{num}\n", fg="red")
                print_file(std_error_path, 2)
                continue

            if check_diff(std_output_path, ans_path):
                click.secho(f"Accepted #{num}\n", fg="green")

                if not is_file_empty(std_error_path):
                    click.secho(f"Standard Error: ", fg="cyan")
                    print_file(std_error_path)
            else:
                click.secho(f"Wrong Answer #{num}\n", fg="red")

                click.secho(f"Test Case: ", fg="cyan")
                print_file(in_path)

                click.secho(f"Correct Answer: ", fg="cyan")
                print_file(ans_path)

                click.secho(f"Standard Output: ", fg="cyan")
                print_file(std_output_path)

                if not is_file_empty(std_error_path):
                    click.secho(f"Standard Error: ", fg="cyan")
                    print_file(std_error_path)
    else:
        click.secho("Enter the input:", fg="cyan")
        if is_interpreted[extension]:
            run_func[extension](
                source_code_path,
                config_data["language"][extension]["command"],
                interactive=True,
            )
        else:
            run_func[extension](exec_path, interactive=True)


def manage(filename, base_folder, config_data, tc, interactive):
    file_path = base_folder / filename
    extension = file_path.suffix[1:]
    filename_without_extension = file_path.stem
    if extension not in ["py", "java", "cpp"]:
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
                filename_without_extension,
                extension,
                base_folder,
                config_data,
                tc,
                interactive,
            )
