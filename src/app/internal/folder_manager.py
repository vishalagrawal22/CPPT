import sys
from pathlib import Path

import click


def delete_folder(path):
    for sub in path.iterdir():
        if sub.is_dir():
            delete_folder(sub)
        else:
            sub.unlink()
    path.rmdir()


def clear_folder(path):
    for sub in path.iterdir():
        if sub.is_dir():
            delete_folder(sub)
        else:
            sub.unlink()


class Task:
    def __init__(self, base_folder, task_name, extension):
        self.source_code = base_folder / task_name
        self.source_code = self.source_code.with_suffix(extension)
        self.cppt_root_folder = base_folder / ".cppt"
        self.task_folder = self.cppt_root_folder / task_name
        self.tc_folder = self.task_folder / "tc"
        self.last_run_folder = self.task_folder / "last_run"

    def create_root(self):
        try:
            self.cppt_root_folder.mkdir()
            click.secho("Created cppt root folder", fg="cyan")
        except Exception:
            click.secho(f"Unable to create cppt root folder",
                        fg="red",
                        err=True)
            sys.exit(1)

    def create_task(self, tests=None):
        if not self.cppt_root_folder.exists():
            self.create_root()
        try:
            self.source_code.touch()
            click.secho("Created source code file", fg="cyan")
        except Exception:
            click.secho(f"Unable to create source code file",
                        fg="red",
                        err=True)
            sys.exit(1)

        try:
            self.task_folder.mkdir()
            click.secho("Created task folder", fg="cyan")
        except Exception:
            click.secho(f"Unable to create task folder", fg="red", err=True)
            sys.exit(1)

        try:
            self.tc_folder.mkdir()
            click.secho("Created tc folder", fg="cyan")
        except Exception:
            click.secho(f"Unable to create tc folder", fg="red", err=True)
            sys.exit(1)

        try:
            self.last_run_folder.mkdir()
            click.secho("Created last run folder", fg="cyan")
        except Exception:
            click.secho(f"Unable to create last run folder",
                        fg="red",
                        err=True)
            sys.exit(1)

        if (tests is not None):
            self.add_tests(tests)
            click.secho("Added Testcases", fg="cyan")

    def add_tests(self, tests):
        try:
            testcase_number = 1
            for individual_testcase in tests:
                is_input_file = 1
                for testcase_element in individual_testcase:
                    prefix = "in" if is_input_file else "ans"
                    with open(
                            self.tc_folder / f"{prefix}{testcase_number}.txt",
                            "w") as file:
                        file.writelines(individual_testcase[testcase_element])
                    is_input_file = is_input_file ^ 1

                testcase_number += 1
        except:
            click.secho(f"Unable to add testcases", fg="red", err=True)
            sys.exit(1)

    def task_exists(self):
        """checks if task exist

        Returns:
            0: neither source code nor test data exists
            1: source code exists
            2: test data exists
            3: both exists
        """
        result = 0
        if self.source_code.exists():
            result = 1

        if self.task_folder.exists():
            if result != 0:
                result = 3
            else:
                result = 2
        return result

    def overwrite(self):
        if self.task_folder.exists():
            try:
                delete_folder(self.task_folder)
                click.secho("Deleted the existing task folder", fg="cyan")
            except:
                click.secho(
                    f"Unable to delete task folder at {self.task_folder}",
                    fg="red",
                    err=True)
                sys.exit(1)

        if self.source_code.exists():
            try:
                self.source_code.unlink()
                click.secho("Deleted the existing source code file", fg="cyan")
            except:
                click.secho(
                    f"Unable to delete source code at {self.source_code}",
                    fg="red",
                    err=True)
                sys.exit(1)
