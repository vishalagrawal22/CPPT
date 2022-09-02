---
title: Edit testcases of task
sidebar_position: 3
---

You can edit testcases related to the task using the `cppt tc edit` command.

It accepts a list of space-separated testcase numbers and loops through each testcase one by one, allowing you to edit their input and output.

It requires multiline input for which it uses an external editor in wait mode. You can configure this editor in the config file (it defaults to vim, If you get stuck in vim use `:q` to exit).

## Usage

```
cppt tc edit --help
```

```shell
Usage: cppt tc edit [OPTIONS] FILENAME [TCS]...

  Edit a set of testcases related to FILENAME

  Args:

  FILENAME of the source code file with file extension
  TCS: space seperated list of test case numbers (0 for all)

Options:
  -p, --path DIRECTORY  path to the folder which contains the souce code
  -h, --help            Show this message and exit.
```

## Demo

![Testcase edit command demo](/gif/tc-edit.gif)
