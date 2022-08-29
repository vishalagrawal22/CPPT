---
title: Delete testcases of task
sidebar_position: 4
---

You can delete testcases related to the task using the `cppt tc delete` command.

It accepts a list of space-separated testcase numbers, deletes all those testcase, and reorders the remaining testcases.

Unlike other tc commands, if you do not specify the `TCS` argument, the delete command fails purposely to prevent you from deleting all testcases by mistake (if you want to delete all testcases, you could enter 0 instead).

## Usage

```shell
cppt tc delete --help
```

```shell
Usage: cppt tc delete [OPTIONS] FILENAME TCS...

  Delete a set of testcases related to FILENAME

  Args:

  FILENAME of the source code file with file extension
  TCS: space seperated list of test case numbers (0 for all)

Options:
  -p, --path DIRECTORY  path to the folder which contains the souce code
  -h, --help            Show this message and exit.
```
