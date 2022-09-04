---
title: Introduction
sidebar_position: 1
---

CPPT is a **cross platform** command line tool to automate your competitive programming workflow **without cluttering** your workspace with testcase data.

## Problem

There already **exist various choices** for command line tools in the competitive programming ecosystem like [cpb](https://searleser97.github.io/cpbooster/) and [cf tool](https://github.com/xalanq/cf-tool), which could help you automate various repetitive tasks and make competitive programming more efficient and fun. The problem with these tools is they follow the **"Flat File Structure" philosophy** in which your source code and testcase files are kept in the same folder to improve the speed of manipulating (creating, updating, deleting) them. This approach causes a mess making it **hard to navigate** between source code files. As changes in testcase are rare, saving a few seconds is manipulating them might not be worth it.

![cpb example](/img/cpb.png)

## Solution

CPPT **hides** all the data required to test your code inside a hidden subfolder (.cppt) so that your **folder remains clean** and you can **focus on writing your source code** instead while providing you with easy-to-use and fast testcase manipulation commands.

![cppt example](/img/cppt.png)

## Getting Started

### Supported Operating Systems

1. Windows (both **cmd** and **wsl**)
2. Linux
3. MacOS

### Supported Languages

1. C++
2. Java
3. Python

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

![Folder Structure Example](/img/folder-structure.png)
