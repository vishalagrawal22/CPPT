import re
import subprocess
import sys
from pathlib import Path

import click

from ...utils.file_manager import (is_file_empty, print_file, read_from_file,
                                   write_to_file)
from ...utils.folder_manager import Task, clear_folder


def get_command(lang):
    pass


def cpp_compile(source_code_path, error_path, command):
    file_name_without_extension = source_code_path.stem
    exec_path = error_path.parent / file_name_without_extension
    command = command.split()
    command.extend([source_code_path, "-o", exec_path])
    compilation_data = subprocess.run(command, capture_output=True, text=True)
    write_to_file(error_path, compilation_data.stderr)

    return [exec_path, compilation_data.returncode]


def cpp_run(exec_path, input_path, output_path, error_path):
    run_data = subprocess.run([exec_path.resolve()],
                              input=read_from_file(input_path),
                              capture_output=True,
                              text=True)
    write_to_file(error_path, run_data.stderr)
    write_to_file(output_path, run_data.stdout)
    return run_data.returncode


def java_compile(source_code_path, error_path, command):
    file_name_without_extension = source_code_path.stem
    last_run_path = error_path.parent
    exec_path = last_run_path / file_name_without_extension
    command = command.split()
    command.extend([source_code_path, "-d", last_run_path])
    compilation_data = subprocess.run(command, capture_output=True, text=True)
    write_to_file(error_path, compilation_data.stderr)

    return [exec_path, compilation_data.returncode]


def java_run(exec_path, input_path, output_path, error_path):
    run_data = subprocess.run(
        ["java", "-cp",
         exec_path.parent.resolve(), exec_path.stem],
        input=read_from_file(input_path),
        capture_output=True,
        text=True)
    write_to_file(error_path, run_data.stderr)
    write_to_file(output_path, run_data.stdout)
    return run_data.returncode


# exec path incase of interpreted language is source code path
def py_run(source_code_path, input_path, output_path, error_path, command):
    command = command.split()
    command.extend([source_code_path])
    run_data = subprocess.run(command,
                              input=read_from_file(input_path),
                              capture_output=True,
                              text=True)
    write_to_file(error_path, run_data.stderr)
    write_to_file(output_path, run_data.stdout)
    return run_data.returncode


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


def judge(task, filename_without_extension, extension, base_folder,
          config_data):
    clear_folder(task.last_run_folder)

    tc_list = task.get_tc_list()

    if tc_list == []:
        click.secho(f"No testcase to run!", fg="red")
        sys.exit(1)

    source_code_path = (base_folder /
                        filename_without_extension).with_suffix("." +
                                                                extension)
    compilation_error_path = task.last_run_folder / "compilation_error.txt"

    exec_path = Path()
    if not is_interpreted[extension]:
        click.secho(f"Compiling the source code with command:", fg="cyan")
        click.secho(config_data["language"][extension]["command"] + "\n")
        exec_path, compile_returncode = compile_func[extension](
            source_code_path, compilation_error_path,
            config_data["language"][extension]["command"])
        if compile_returncode != 0:
            click.secho(f"Compilation Error:\n", fg="red")
            print_file(compilation_error_path, True)
            sys.exit()
        else:
            click.secho(f"Compiled Successfully\n", fg="green")
            if not is_file_empty(compilation_error_path):
                click.secho(f"Compilation Warning:\n", fg="cyan")
                print_file(compilation_error_path)
    else:
        click.secho(f"Running the source code with command:", fg="cyan")
        click.secho(config_data["language"][extension]["command"] + "\n")

    for num in tc_list:
        in_path = task.tc_folder / f"in{num}.txt"
        ans_path = task.tc_folder / f"ans{num}.txt"
        diff_path = task.last_run_folder / f"diff{num}.txt"
        std_output_path = task.last_run_folder / f"output{num}.txt"
        std_error_path = task.last_run_folder / f"error{num}.txt"

        click.secho(f"Running TC #{num}\n", fg="cyan")

        run_returncode = 0
        if is_interpreted[extension]:
            run_returncode = run_func[extension](
                source_code_path, in_path, std_output_path, std_error_path,
                config_data["language"][extension]["command"])
        else:
            run_returncode = run_func[extension](exec_path, in_path,
                                                 std_output_path,
                                                 std_error_path)

        if run_returncode != 0:
            click.secho(f"Rumtime Error #{num}\n", fg="red")
            print_file(std_error_path, True)
            continue

        diff_command = ["diff", "-b", "-B", std_output_path, ans_path]
        run_diff_data = subprocess.run(diff_command,
                                       capture_output=True,
                                       text=True)
        with open(diff_path, "w") as file:
            file.writelines(run_diff_data.stdout)

        if (is_file_empty(diff_path)):
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


def manage(filename, base_folder, config_data):
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
                click.secho("Neither source code nor test data exists",
                            err=True,
                            fg="red")
            elif task_status == 1:
                click.secho("Test Data does not exist", err=True, fg="red")
            elif task_status == 2:
                click.secho("Source Code does not exist", err=True, fg="red")

            click.secho(
                "Try overwriting existing files with create or fetch commands's --force option",
                err=True,
                fg="red")
            click.secho(
                "Caution: do not forget to copy any code in source file before using --force option",
                err=True,
                fg="red")
            sys.exit(1)

        judge(task, filename_without_extension, extension, base_folder,
              config_data)
