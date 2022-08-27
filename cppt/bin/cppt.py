from pathlib import Path

import click
import sys

from ..commands import (
    compile_manage,
    config_manage,
    create_manage,
    fetch_manage,
    run_manage,
    test_manage,
    view_tc_manage,
    add_tc_manage,
    edit_tc_manage,
    delete_tc_manage,
)

from ..utils.config_manager import get_config_data

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    global config_data
    config_data = get_config_data()


@cli.command("create", short_help="create a task")
@click.argument("filename", type=str)
@click.option(
    "-p",
    "--path",
    "base_folder",
    default=None,
    type=click.Path(exists=True, path_type=Path, writable=True, file_okay=False),
    help="path to the folder where you want to create the source code file",
)
@click.option("-f", "--force", is_flag=True, help="overwrite existing files of task")
def create(filename, base_folder, force):
    """
    \b
    Create a task to add and run testcases

    \b
    Args:

    \b
    FILENAME of the file to be created with file extension
    """
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])
    create_manage(filename, base_folder, force, config_data)


@cli.command("fetch", short_help="retrieve testcase data from online judge")
@click.option(
    "-p",
    "--path",
    "base_folder",
    default=None,
    type=click.Path(exists=True, path_type=Path, writable=True, file_okay=False),
    help="path to the folder where you want to create the source code file",
)
@click.option("-f", "--force", is_flag=True, help="overwrite existing files of task")
def fetch(base_folder, force):
    """
    \b
    Retrieve testcase data from online judge,
    make the source code file,
    and copy boiler plate code if specified in config file
    """
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])
    fetch_manage(base_folder, force, config_data)


@cli.command("run", short_help="run code against testcases")
@click.argument("filename", type=str)
@click.option(
    "-p",
    "--path",
    "base_folder",
    default=None,
    type=click.Path(exists=True, path_type=Path, writable=True, file_okay=False),
    help="path to the folder which contains the souce code",
)
@click.option(
    "-t",
    "--tc",
    "tc_no",
    default=0,
    show_default=True,
    help="run specific testcase (0 for all)",
)
@click.option(
    "-i",
    "--interactive",
    is_flag=True,
    help="run program in interactive mode(stdin, stdout, stderr are used)",
)
def run(filename, base_folder, tc_no, interactive):
    """
    \b
    Compile (if applied) and run source code on saved testcases
    using commands specified in the config file

    \b
    Args:

    \b
    FILENAME of the file to run with file extension
    """
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])
    run_manage(filename, base_folder, config_data, tc_no, interactive)


@cli.command("compile", short_help="compile source code")
@click.argument("filename", type=str)
@click.option(
    "-p",
    "--path",
    "base_folder",
    default=None,
    type=click.Path(exists=True, path_type=Path, writable=True, file_okay=False),
    help="path to the folder which contains the souce code",
)
def compile(filename, base_folder):
    """
    \b
    Compile (if applied) the source code
    using commands specified in the config file

    \b
    Args:

    \b
    FILENAME of the file to run with file extension
    """
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])
    compile_manage(filename, base_folder, config_data)


@cli.group(short_help="commands related to testcase data")
def tc():
    pass


def get_cleaned_tcs(tcs):
    cleaned_tcs = []

    has_zero = len(tcs) == 0
    for currentTc in tcs:
        if int(currentTc) == 0:
            has_zero = True
        else:
            cleaned_tcs.append(int(currentTc))

    if has_zero:
        cleaned_tcs = [0]

    cleaned_tcs = list(set(cleaned_tcs))
    cleaned_tcs.sort()
    return cleaned_tcs


@tc.command(short_help="view testcases")
@click.argument("filename", type=str)
@click.option(
    "-p",
    "--path",
    "base_folder",
    default=None,
    type=click.Path(
        exists=True,
        path_type=Path,
        writable=True,
        file_okay=False,
    ),
    help="path to the folder which contains the souce code",
)
@click.argument("tcs", nargs=-1)
def view(filename, base_folder, tcs):
    """
    \b
    View a set of testcases related to FILENAME

    \b
    Args:

    \b
    FILENAME of the source code file with file extension
    TCS: space seperated list of test case numbers (0 for all)
    """
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])

    view_tc_manage(filename, base_folder, get_cleaned_tcs(tcs))


@tc.command(short_help="add testcase")
@click.argument("filename", type=str)
@click.option(
    "-p",
    "--path",
    "base_folder",
    default=None,
    type=click.Path(
        exists=True,
        path_type=Path,
        writable=True,
        file_okay=False,
    ),
    help="path to the folder which contains the souce code",
)
def add(filename, base_folder):
    """
    \b
    Add a testcase to FILENAME

    \b
    Args:

    \b
    FILENAME of the source code file with file extension
    """
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])

    editor = None
    if "multiline_input_command" in config_data:
        editor = config_data["multiline_input_command"]

    add_tc_manage(filename, base_folder, editor)


@tc.command(short_help="edit testcases")
@click.argument("filename", type=str)
@click.option(
    "-p",
    "--path",
    "base_folder",
    default=None,
    type=click.Path(
        exists=True,
        path_type=Path,
        writable=True,
        file_okay=False,
    ),
    help="path to the folder which contains the souce code",
)
@click.argument("tcs", nargs=-1)
def edit(filename, base_folder, tcs):
    """
    \b
    Edit a set of testcases related to FILENAME

    \b
    Args:

    \b
    FILENAME of the source code file with file extension
    TCS: space seperated list of test case numbers (0 for all)
    """
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])

    editor = None
    if "multiline_input_command" in config_data:
        editor = config_data["multiline_input_command"]

    edit_tc_manage(filename, base_folder, get_cleaned_tcs(tcs), editor)


@tc.command(short_help="delete testcases")
@click.argument("filename", type=str)
@click.option(
    "-p",
    "--path",
    "base_folder",
    default=None,
    type=click.Path(
        exists=True,
        path_type=Path,
        writable=True,
        file_okay=False,
    ),
    help="path to the folder which contains the souce code",
)
@click.argument("tcs", nargs=-1, required=True)
def delete(filename, base_folder, tcs):
    """
    \b
    Delete a set of testcases related to FILENAME

    \b
    Args:

    \b
    FILENAME of the source code file with file extension
    TCS: space seperated list of test case numbers (0 for all)
    """
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])

    delete_tc_manage(filename, base_folder, get_cleaned_tcs(tcs))


@cli.command("test", short_help="brute force testing")
@click.argument("filename", type=str)
@click.argument(
    "testcase-generator-path",
    type=click.Path(exists=True, path_type=Path, dir_okay=False),
)
@click.option(
    "-n",
    "--number-of-runs",
    default=10000,
    show_default=True,
    help="no of randomly generated testcases",
)
@click.option(
    "-p",
    "--path",
    "base_folder",
    default=None,
    type=click.Path(
        exists=True,
        path_type=Path,
        writable=True,
        file_okay=False,
    ),
    help="path to the folder which contains the souce code",
)
def test(filename, number_of_runs, testcase_generator_path, base_folder):
    """
    \b
    Generate random testcases and run your code against them.
    Create a function in your source code which validates
    your answer if the validation fails print your answer to
    std output.
    \b
    Args:

    \b
    FILENAME of the source code file with file extension
    TESTCASE_GENERATOR_PATH: path of test case generator file
    """
    if base_folder is None:
        base_folder = Path(config_data["default_base_folder"])
    test_manage(
        filename, number_of_runs, testcase_generator_path, base_folder, config_data
    )


@cli.command("config", short_help="get location of config file or reset config file")
@click.option("--reset", "-r", is_flag=True, help="reset config file to default values")
def config(reset):
    """
    \b
    Locate config file or reset config to default values with --reset option
    """
    config_manage(reset)
