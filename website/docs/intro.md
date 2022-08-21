---
title: Introduction
sidebar_position: 1
---

CPPT is a cross platform command line tool to automate your competitive programming workflow without cluttering your workspace with test case data.

## Problem

There are various choices for command line tools in the competitive programming ecosystem like [cpb](https://searleser97.github.io/cpbooster/) and [cf tool](https://github.com/xalanq/cf-tool), which could help you automate various repetitive tasks and make competitive programming more efficient and fun but these tools can fill your source code directory with test case files quickly. If you like to solve many problems from various platforms without changing your work directory, this causes a big mess.

## Solution

CPPT hides all the data required to test your code inside a hidden folder (.cppt) so that your directory remains clean and you can focus on writing your source code instead.

## Getting Started

### Supported Operating Systems

1. Windows (both cmd and wsl)
2. Linux
3. MacOS

### Requirements

1. Python version >= 3.6 and pip installed
2. [Competitive companion](https://github.com/jmerle/competitive-companion) browser extension installed.

### Installation

Use the following command to install the tool

```shell
$ pip install cppt
```

After the tool is installed, type the command

```shell
$ cppt
```

you should see the following help text.

```
Usage: cppt [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  addtc    add a tc to be used in future runs of code
  compile  compile source code
  config   get location of config file or reset config file
  create   create a task
  fetch    retrieve testcase data from online judge
  run      run code against testcases
  test     brute force testing
```
