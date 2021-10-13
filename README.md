# Competitive Programming Practice Tool

A command-line tool to automate your competitive programming workflow without cluttering your workspace with test case data.

## Setup Guide

Make sure you have python version >= 3.6 and pip installed.
In case you do not know about installing packages in python you can check out
https://packaging.python.org/tutorials/installing-packages/.

After getting everything ready,
simply type the command `pip install cppt` to install the tool

After the tool is installed type the command `cppt`

you should see the following help text.

![help text cppt](https://i.imgur.com/bOASG2a.png)

To fetch test case data from an online judge, you will need [competitive companion](https://github.com/jmerle/competitive-companion) browser extension.

## Features
1. Fetch test case data from an online judge.
2. Compile (if applied) and run source code against the aforementioned test cases.
3. Add your test cases to run your code on.
4. Create a source code file with your saved templates.

## Developer Guide
If you want to experiment with the project
you need [pyenv](https://realpython.com/intro-to-pyenv/)  and [pipenv](https://realpython.com/pipenv-guide/)

1. clone the repo
2. cd into the created folder,
3. then use the command `pipenv install -e . --dev`
