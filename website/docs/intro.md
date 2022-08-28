---
title: Introduction
sidebar_position: 1
---

CPPT is a cross platform command line tool to automate your competitive programming workflow without cluttering your workspace with testcase data.

## Problem

There are various choices for command line tools in the competitive programming ecosystem like [cpb](https://searleser97.github.io/cpbooster/) and [cf tool](https://github.com/xalanq/cf-tool), which could help you automate various repetitive tasks and make competitive programming more efficient and fun but these tools can fill your source code directory with testcase files quickly. If you like to solve many problems from various platforms without changing your work directory, this causes a big mess.

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
  compile  compile source code
  config   get location of config file or reset config file
  create   create a task
  fetch    retrieve testcase data from online judge
  run      run code against testcases
  tc       commands related to testcase data
  test     brute force testing
```

### Folder structure

CPPT creates a hidden root folder (.cppt) in every directory where you use **_fetch_** or **_create_** commands to create tasks.

Every task you create has a dedicated subfolder that shares the same name as the task.

Each task folder consists of a **_tc folder_** and a **_last_run folder_** respectively.

The **_tc folder_** consists of all the input files (in{num}.txt) and all the intended output files (ans{num}.txt).

The **_last_run folder_** consists of all files generated in the last run like the standard output files (output{num}.txt), standard error files (error{num}.txt), and compilation_error.txt which consist of the compilation error text if any.

You can use the **standard error** (like cerr in c++) to **print debugging info**. It will be displayed separately and will not affect the testcase verdict (only standard output needs to match the intended output to get accepted).

Example from Meta Hacker Cup 2022 Qualification Round (using `tree -a .` command) :-

```shell
.
├── .cppt
│   ├── A_Second_Hands
│   │   ├── last_run
│   │   │   ├── compilation_error.txt
│   │   │   ├── error1.txt
│   │   │   └── output1.txt
│   │   └── tc
│   │       ├── ans1.txt
│   │       └── in1.txt
│   ├── B2_Second_Second_Friend
│   │   ├── last_run
│   │   │   ├── compilation_error.txt
│   │   │   ├── error1.txt
│   │   │   ├── error2.txt
│   │   │   ├── output1.txt
│   │   │   └── output2.txt
│   │   └── tc
│   │       ├── ans1.txt
│   │       ├── ans2.txt
│   │       ├── in1.txt
│   │       └── in2.txt
```
