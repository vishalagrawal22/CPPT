---
title: Add testcase to task
sidebar_position: 1
---

You can add your testcases to be used in future runs of your source code using the `cppt tc add` command.

It requires multiline input for which it uses an external editor in wait mode to take input. You can configure this editor in the config file (it defaults to vim, If you get stuck in vim use `:q` to exit).

You can add a single testcase at a time (for each execution of the command) for now.

## Usage

```shell
cppt tc add --help
```

```shell
Usage: cppt tc add [OPTIONS] FILENAME

  Add a testcase to FILENAME

  Args:

  FILENAME of the source code file with file extension

Options:
  -p, --path DIRECTORY  path to the folder which contains the souce code
  -h, --help            Show this message and exit.
```

## Demo
