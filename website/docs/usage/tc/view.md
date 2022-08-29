---
title: View testcases of task
sidebar_position: 2
---

You can view testcases related to the task using the `cppt tc view` command.

It accepts a list of space-separated testcase numbers and prints the corresponding testcase data.

## Usage

```
cppt tc view --help
```

```shell
Usage: cppt tc view [OPTIONS] FILENAME [TCS]...

  View a set of testcases related to FILENAME

  Args:

  FILENAME of the source code file with file extension
  TCS: space seperated list of test case numbers (0 for all)

Options:
  -p, --path DIRECTORY  path to the folder which contains the souce code
  -h, --help            Show this message and exit.
```
