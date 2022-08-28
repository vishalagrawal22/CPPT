---
title: Configuration
sidebar_position: 2
---

CPPT utilizes the YAML language for the config file instead of the typical JSON format because YAML is more readable and allows adding comments in the config file to improve your experience when dealing with them.

## Location

The config file should be located at `~/.config/cppt/config.yaml`.

## Create default config file

The config file gets automatically created whenever you run a command. If you want to manually create a config file, type the following command.

```shell
$ cppt config
```

If you want to override the current config file with default values use the following command.

```shell
$ cppt config --reset
```

## Default config file

```yaml
# absolute or relative path to the folder
# where you want the source code (folder should already exist)
# example: ~/cp/practice (saves code to $HOME/cp/practice)
# default: current directory
default_base_folder: .

# the file extension of source code file created by cppt fetch command
# valid options: cpp, py, java
# default: cpp
default_language: cpp

# programming language related settings

# command represents the command used to compile or run your source code

# template represents
# absolute path to your boiler plate code for the particular language
# the boiler plate code will be copied to the source code of that language
# which were created by cppt (fetch or create commands)
# example: ~/cp/templates/template.cpp
# default: empty file

language:
  cpp:
    # do not include -o flag
    command: g++ -std=gnu++17 -O2 -Wall -Wextra -Wshadow
    template: null

  java:
    # do not include -cp flag
    command: javac
    template: null

  py:
    command: python3
    template: null

# command which you use to open your editor
# for vscode: code
# for sublime: subl
editor: null

# command to open editor for multiline input
# for vscode: code --wait
# for sublime: subl --wait
multiline_input_command: null
```
