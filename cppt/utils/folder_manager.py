import sys

import click

from .file_manager import read_from_file, write_to_file


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
            click.secho("Unable to create cppt root folder", fg="red", err=True)
            sys.exit(1)

    def create_task(self, tests=None, template_path=None, create_source_code=True):
        if not self.cppt_root_folder.exists():
            self.create_root()

        if create_source_code:
            try:
                self.source_code.touch()
                if template_path is not None:
                    write_to_file(self.source_code, read_from_file(template_path))
                click.secho("Created source code file", fg="cyan")
            except Exception:
                click.secho("Unable to create source code file", fg="red", err=True)
                sys.exit(1)

        try:
            self.task_folder.mkdir()
            self.tc_folder.mkdir()
            self.last_run_folder.mkdir()
            click.secho("Created task folder", fg="cyan")
        except Exception:
            click.secho("Unable to create task folder", fg="red", err=True)
            sys.exit(1)

        if tests is not None:
            self.add_tests(tests)
            click.secho("Created testcase files", fg="cyan")

    def add_tests(self, tests, tc_number=1):
        try:
            testcase_number = tc_number
            for test in tests:
                self.add_test(test, testcase_number)
                testcase_number += 1

        except Exception:
            click.secho("Unable to add testcases", fg="red", err=True)
            sys.exit(1)

    def add_test(self, test, tc_number=None):
        try:
            if tc_number is None:
                tc_list = self.get_tc_list()
                tc_number = 1
                if len(tc_list) != 0:
                    tc_number = tc_list[-1] + 1

            with open(
                self.tc_folder / f"in{tc_number}.txt",
                "w",
                encoding="utf-8",
            ) as file:
                file.writelines(test["input"])

            with open(
                self.tc_folder / f"ans{tc_number}.txt",
                "w",
                encoding="utf-8",
            ) as file:
                file.writelines(test["output"])
        except Exception:
            click.secho(f"Unable to add testcase #{tc_number}", fg="red", err=True)
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
                click.secho("Deleted the existing task folder", fg="red")
            except Exception:
                click.secho(
                    f"Unable to delete task folder at {self.task_folder.resolve()}",
                    fg="red",
                    err=True,
                )
                sys.exit(1)

        if self.source_code.exists():
            try:
                self.source_code.unlink()
                click.secho("Deleted the existing source code file", fg="red")
            except Exception:
                click.secho(
                    f"Unable to delete source code at {self.source_code.resolve()}",
                    fg="red",
                    err=True,
                )
                sys.exit(1)

    def safe_overwrite(self, force):
        task_status = self.task_exists()
        if task_status != 0:
            if not force:
                if task_status == 1:
                    click.secho(
                        f"Source code already exists at {self.source_code.resolve()}",
                        err=True,
                        fg="red",
                    )
                elif task_status == 2:
                    click.secho(
                        f"Task folder already exists at {self.task_folder.resolve()}",
                        err=True,
                        fg="red",
                    )
                else:
                    click.secho(
                        f"Both source code and task folder already exists at {self.source_code.resolve()} and {self.task_folder.resolve()} respectively",
                        err=True,
                        fg="red",
                    )

                click.secho(
                    "To overwrite existing files specify --force option",
                    err=True,
                    fg="red",
                )
                sys.exit(1)
            else:
                self.overwrite()

    def get_tc_list(self):
        tc_set = set()
        for tc in self.tc_folder.iterdir():
            tc = tc.name
            if tc.startswith("in"):
                num = int(tc[2:][:-4])
                tc_set.add(num)
            elif tc.startswith("ans"):
                num = int(tc[3:][:-4])
                tc_set.add(num)

        tc_list = []
        for tc in tc_set:
            tc_list.append(tc)

        tc_list.sort()
        return tc_list

    def get_tc(self, tc_no):
        tc_list = self.get_tc_list()

        if tc_no not in tc_list:
            return None

        return {
            "input": read_from_file(self.tc_folder / f"in{tc_no}.txt"),
            "output": read_from_file(self.tc_folder / f"ans{tc_no}.txt"),
        }

    def get_tcs(self, tc_nos):
        tc_data = []
        for tc_no in tc_nos:
            tc_data.append(self.get_tc(tc_no))
        return tc_data

    def edit_tc(self, tc_no, tc):
        with open(
            self.tc_folder / f"in{tc_no}.txt",
            "w",
            encoding="utf-8",
        ) as file:
            file.writelines(tc["input"])

        with open(
            self.tc_folder / f"ans{tc_no}.txt",
            "w",
            encoding="utf-8",
        ) as file:
            file.writelines(tc["output"])

    def edit_tcs(self, tc_nos, tcs):
        for tc_no, tc in zip(tc_nos, tcs):
            self.edit_tc(tc_no, tc)

    def clear_tcs(self):
        clear_folder(self.tc_folder)


def exit_if_invalid_extension(extension):
    if extension not in ["py", "java", "cpp"]:
        click.secho(
            f"Language {extension} is not supported (python(py), java, c++(cpp) are only supported)",
            err=True,
            fg="red",
        )
        sys.exit(1)


def exit_if_invalid_task(task):
    task_status = task.task_exists()
    if task_status != 3:
        if task_status == 0:
            click.secho(
                f"Neither source code nor task folder exists at {task.source_code.resolve()} and {task.task_folder.resolve()} respectively",
                err=True,
                fg="red",
            )
        elif task_status == 1:
            click.secho(
                f"Task folder does not exist at {task.task_folder.resolve()}",
                err=True,
                fg="red",
            )
        elif task_status == 2:
            click.secho(
                f"Source code does not exist at {task.source_code.resolve()}",
                err=True,
                fg="red",
            )

        click.secho(
            "Try overwriting existing files with create or fetch commands's --force option",
            err=True,
            fg="red",
        )
        click.secho(
            "Caution: do not forget to copy any code in source file before using --force option",
            err=True,
            fg="red",
        )
        sys.exit(1)
