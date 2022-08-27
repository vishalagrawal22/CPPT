import click

from ...utils.file_manager import open_source_code_in_editor
from ...utils.folder_manager import Task
from .server import get_task_data


def get_file_name(task_name):
    name_char_list = []
    last_was_alnum = 0
    for ch in task_name:
        if ch.isalnum():
            name_char_list.append(ch)
            last_was_alnum = 1
        else:
            if last_was_alnum:
                name_char_list.append("_")
            last_was_alnum = 0
    return "".join(name_char_list)


def manage(base_folder, force, config_data):
    task_data = get_task_data()
    testData = task_data["tests"]
    tests = []
    for individual_testcase in testData:
        test = {}
        is_input_file = True
        for testcase_element in individual_testcase:
            if is_input_file:
                test["input"] = individual_testcase[testcase_element]
            else:
                test["output"] = individual_testcase[testcase_element]
            is_input_file = not is_input_file
        tests.append(test)

    filename_without_extension = get_file_name(task_data["name"])
    extension = config_data["default_language"]

    task = Task(base_folder, filename_without_extension, extension)
    task.safe_overwrite(force)
    task.create_task(tests, config_data["language"][extension]["template"])
    click.secho("Successfully created task", fg="green")
    click.secho(f"Source code is located at {task.source_code.resolve()}", fg="green")
    open_source_code_in_editor(config_data, task.source_code)
