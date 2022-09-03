---
title: Compile task
sidebar_position: 6
---

To compile a source code using the command specified in the config file, use the `cppt compile` command.

It will create an executable in the same directory as your source code.

Note: you don't need to use the compile command before the run command (the run command handles compilation by itself). The compile command is present to give you low-level control of the executable for things like generating output files for competitions like Meta HackerCup etc.

## Usage

```shell
cppt compile --help
```

```shell
Usage: cppt compile [OPTIONS] FILENAME

  Compile (if applied) the source code
  using commands specified in the config file

  Args:

  FILENAME of the file to run with file extension

Options:
  -p, --path DIRECTORY  path to the folder which contains the souce code
  -h, --help            Show this message and exit.
```

## Demo

![Compile command demo](/gif/compile.gif)
