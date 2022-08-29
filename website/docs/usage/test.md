---
title: Stress test task
sidebar_position: 4
---

CPPT can help you stress test your code against randomly generated testcases.

You should create a random testcase generator code to test your source code. This code should output a single random testcase file every time you run it (for better results, try using smaller constraints on the range of values in the testcase).

You should add a **validator** function in your source code file, which could be a brute force solution, editorial code, or an output correctness checker. If your validator states that your output is **incorrect**, you should use the **standard output** (cout in c++) to print any **debugging info** that will **stop** the command execution (it is **mandatory** to print something to the standard output to state the source code failed) and displays the testcase. If your output is **correct**, then do **not** print anything to the **standard output**. It would result in command termination instead use the **standard error** (cerr in c++).

Currently, the testing speed of this command is slow, so if you are using a Unix operating system. I would recommend checking out [Errichto's video](https://www.youtube.com/watch?v=JXTVOyQpSGM) on stress testing and [my Github repo](https://github.com/vishalagrawal22/TestCaseGenerator) for doing the same using bash script.

## Usage

```shell
cppt test --help
```

```shell
Usage: cppt test [OPTIONS] FILENAME TESTCASE_GENERATOR_PATH

  Generate random testcases and run your code against them.
  Create a function in your source code which validates
  your answer if the validation fails print your answer to
  std output.

  Args:

  FILENAME of the source code file with file extension
  TESTCASE_GENERATOR_PATH: path of test case generator file

Options:
  -n, --number-of-runs INTEGER  no of randomly generated testcases  [default:
                                10000]
  -p, --path DIRECTORY          path to the folder which contains the souce
                                code
  -h, --help                    Show this message and exit.
```
