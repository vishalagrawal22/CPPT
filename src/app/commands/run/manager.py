import sys
import click
import subprocess

from pathlib import Path

from ...internal.folder_manager import Task

def get_command(language):
    pass

def cpp_compile(source_code_path, exec_path, compilation_error_path):
    subprocess_data = subprocess.run(["g++-11", source_code_path, "-o", exec_path], capture_output=True, text=True)
    with open(compilation_error_path, "w") as file:
        file.writelines(subprocess_data.stderr)
    return subprocess_data.returncode

# def java_compile(source_code_path, exec_path, compilation_error_path):
#     subprocess_data = subprocess.run(["javac", exec_path], capture_output=True, text=True)
#     with open(compilation_error_path, "w") as file:
#         file.writelines(subprocess_data.stderr)
#     return subprocess_data.returncode

def py_compile():
    # just an empty function to avoid errors
    return 0

def cpp_run(exec_path, in_path, std_error_path, std_output_path):
    infile = open(in_path, 'r')
    in_txt = "".join(infile.readlines())
    subprocess_data = subprocess.run([f"./{exec_path}"], input=in_txt, encoding='ascii', capture_output=True, text=True)
    with open(std_error_path, "w") as file:
        file.writelines(subprocess_data.stderr)

    with open(std_output_path, "w") as file:
        file.writelines(subprocess_data.stdout)

    return subprocess_data.returncode

def java_run(exec_path, in_path, std_error_path, std_output_path):
    infile = open(in_path, 'r')
    in_txt = "".join(infile.readlines())
    subprocess_data = subprocess.run([f"java {exec_path}"], input=in_txt, encoding='ascii', capture_output=True, text=True)
    with open(std_error_path, "w") as file:
        file.writelines(subprocess_data.stderr)

    with open(std_output_path, "w") as file:
        file.writelines(subprocess_data.stdout)

    return subprocess_data.returncode

def py_run():
    pass

run_func = {
            ".py": py_run, 
            ".java": java_run, 
            ".cpp": cpp_run,
}

compile_func = {
            ".py": py_compile, 
            ".java": java_compile, 
            ".cpp": cpp_compile,
}

def print_file(file_path, error=False):
    if not file_path.exists():
        click.secho(f"File at {file_path} does not exist", fg="red", err=True)
        sys.exit(1)
    elif not file_path.is_file():
        click.secho(f"{file_path} is not a file", fg="red", err=True)
        sys.exit(1)

    with open(file_path, 'r') as file:
        for line in file.readlines():
            click.secho(line, fg="red", err=error, nl=False)
    click.echo("")
        


def judge(task, filename_without_extension, extension, base_folder):
    tc_list = []
    for tc in task.tc_folder.iterdir():
        tc = tc.name
        if (tc.startswith("in")):
            num = int(tc[2:][:-4])
            ans_path = task.tc_folder / f"ans{num}.txt"
            if ans_path.is_file():
                tc_list.append(num)

    tc_list.sort()

    source_code_path = (base_folder / filename_without_extension).with_suffix(extension)
    exec_path = base_folder / f"{filename_without_extension}"
    compilation_error_path = task.last_run_folder / "compilation_error.txt"

    if compile_func[extension](source_code_path, exec_path, compilation_error_path) != 0:
        click.secho(f"Compilation Error:\n", fg="red")
        print_file(compilation_error_path, True)
        sys.exit(1)

    for num in tc_list:
        in_path = task.tc_folder / f"in{num}.txt"
        ans_path = task.tc_folder / f"ans{num}.txt"
        diff_path = task.last_run_folder / f"diff{num}.txt"
        std_output_path = task.last_run_folder / f"output{num}.txt"
        std_error_path = task.last_run_folder / f"error{num}.txt"
        runtime_error_path = task.last_run_folder / f"runtime_error{num}.txt"

        click.secho(f"Running TC #{num}\n", fg="cyan")

        if run_func[extension](exec_path, in_path, std_error_path, std_output_path) != 0:
            click.secho(f"Rumtime Error #{num}\n", fg="red")
            continue
                

        diff_command = ["diff", "-b", "-B", std_output_path, ans_path]
        run_diff_data = subprocess.run(diff_command, capture_output=True, text=True)
        with open(diff_path, "w") as file:
            file.writelines(run_diff_data.stdout)

        if (diff_path.stat().st_size == 0):
            click.secho(f"Accepted #{num}\n", fg="green")

            if std_error_path.stat().st_size != 0:
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

            if std_error_path.stat().st_size != 0:
                click.secho(f"Standard Error: ", fg="cyan")
                print_file(std_error_path)

def manage(filename, base_folder):
    file_path = base_folder / filename
    extension = file_path.suffix
    filename_without_extension = file_path.stem
    if extension not in [".py", ".java", ".cpp"]:
        click.secho(f"Language {file_path.suffix} is not supported (.py, .java, .cpp are only supported)", err=True, fg="red")
        sys.exit(1)
    else:
        task = Task(base_folder, filename_without_extension, extension)
        task_status = task.task_exists()
        if task_status != 3:
            if task_status == 0:
                click.secho("Neither source code nor test data exists", err=True, fg="red")
            elif task_status == 1:
                click.secho("Test Data does not exist", err=True, fg="red")
            elif task_status == 2:
                click.secho("Source Code does not exist", err=True, fg="red")
            
            click.secho("Try overwriting existing files with create or fetch commands's --force option", err=True, fg="red")
            click.secho("Caution: do not forget to copy any code in source file before using --force option", err=True, fg="red")
            sys.exit(1)

        judge(task, filename_without_extension, extension, base_folder)

        

        