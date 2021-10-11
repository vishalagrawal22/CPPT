import sys
from pathlib import Path

import click

from ..utils.file_manager import read_from_file, write_to_file


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
        self.source_code = self.source_code.with_suffix("." + extension)
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

    def create_task(self, tests=None, template_path=None):
        if not self.cppt_root_folder.exists():
            self.create_root()
        try:
            self.source_code.touch()
            if template_path is not None:
                write_to_file(self.source_code, read_from_file(template_path))
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

    def add_tests(self, tests, tc_number=1):
        try:
            testcase_number = tc_number
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
                    f"Unable to delete task folder at {self.task_folder.resolve()}",
                    fg="red",
                    err=True)
                sys.exit(1)

        if self.source_code.exists():
            try:
                self.source_code.unlink()
                click.secho("Deleted the existing source code file", fg="cyan")
            except:
                click.secho(
                    f"Unable to delete source code at {self.source_code.resolve()}",
                    fg="red",
                    err=True)
                sys.exit(1)

    def safe_overwrite(self, force):
        task_status = self.task_exists()
        if task_status != 0:
            if not force:
                if task_status == 1:
                    click.secho(
                        f"Source code already exists at {self.source_code.resolve()}",
                        err=True,
                        fg="red")
                elif task_status == 2:
                    click.secho(
                        f"Task folder already exists at {self.task_folder.resolve()}",
                        err=True,
                        fg="red")
                else:
                    click.secho(
                        f"Both source code and task folder already exists at {self.source_code.resolve()} and {self.task_folder.resolve()} respectively",
                        err=True,
                        fg="red")

                click.secho(
                    "To overwrite existing files specify --force option",
                    err=True,
                    fg="red")
                sys.exit(1)
            else:
                self.overwrite()

    def get_tc_list(self):
        tc_list = []
        for tc in self.tc_folder.iterdir():
            tc = tc.name
            if (tc.startswith("in")):
                num = int(tc[2:][:-4])
                ans_path = self.tc_folder / f"ans{num}.txt"
                if ans_path.is_file():
                    tc_list.append(num)
        tc_list.sort()
        return tc_list
