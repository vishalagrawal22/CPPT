---
title: Fetch testcase data
sidebar_position: 1
---

You can fetch testcase data for any problem (fetching the entire contest at once is **not** supported for now) using the `cppt fetch` command and [competitive companion](https://github.com/jmerle/competitive-companion) browser extension. It creates the source file which uses the extension mentioned in the config file (defaults to cpp) and copies your template code into the source file.

## Usage

```shell
$ cppt fetch --help
```

```shell
Usage: cppt fetch [OPTIONS]

  Retrieve testcase data from online judge,
  make the source code file,
  and copy boiler plate code if specified in config file

Options:
  -p, --path DIRECTORY  path to the folder where you want to create the source
                        code file
  -f, --force           overwrite existing files of task
  -h, --help            Show this message and exit.
```

## Demo
