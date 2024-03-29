---
title: Run task
sidebar_position: 2
---

You can compile (if applicable) and run your source code using the `cppt run` command. It uses the command specified in the config file to run your source code. It supports running C++, Java, and Python source files.

You can run your source code against:-

1. all testcases
2. specific testcase
3. interactively entered testcase

The _run_ command supports the following verdicts:-

1. Accepted
2. Wrong answer
3. Compilation error
4. Runtime error

You can use the **standard error** (like cerr in c++) to **print debugging info**. It will be displayed separately and will not affect the testcase verdict (only standard output needs to match the intended output to get accepted).

## Usage

```shell
$ cppt run --help
```

```shell
Usage: cppt run [OPTIONS] FILENAME

  Compile (if applicable) and run source code on saved testcases
  using commands specified in the config file

  Args:

  FILENAME of the file to run with file extension

Options:
  -p, --path DIRECTORY  path to the folder which contains the souce code
  -t, --tc INTEGER      run specific testcase (0 for all)  [default: 0]
  -i, --interactive     run program in interactive mode(stdin, stdout, stderr
                        are used)
  -h, --help            Show this message and exit.
```

## Demo

![Run command demo](/gif/run.gif)
