---
title: Create task
sidebar_position: 5
---

To create a task manually rather than fetching it from an online judge, use the `cppt create` command.

It would create a source code file with your template code and allow you to add testcases (using `cppt tc add`) to it for future runs.

## Usage

```shell
cppt create -h
```

```shell
Usage: cppt create [OPTIONS] FILENAME

  Create a task to add and run testcases

  Args:

  FILENAME of the file to be created with file extension

Options:
  -p, --path DIRECTORY  path to the folder where you want to create the source
                        code file
  -f, --force           overwrite existing files of task
  -h, --help            Show this message and exit.
```
