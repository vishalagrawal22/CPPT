---
title: Fetch test case data
sidebar_position: 1
---

You can fetch test case data for any problem (fetching the entire contest at once is not supported for now) using the fetch command and [competitive companion](https://github.com/jmerle/competitive-companion) browser extension.

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
