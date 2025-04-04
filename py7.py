#!/usr/bin/env python3
#

"""
File: py7.py "PI-seven" or π-7

Author: William F. Gilreath (will@wfgilreath.xyz)

Date: 03-30-2025

Description: This Python app uses seven Python lint tools to check Python
source code. The seven tools are:

    bandit    - Bandit is a tool designed to find common security
                issues in Python source code.
    mccabe    - Check McCabe complexity in Python source code.
    mypy      - Mypy is a static type checker for Python source code.
    pyflakes  - Pyflakes checks source files for errors in Python
                source code.
    pylint    - Pylint analyses and checks for errors in Python source code.
    ruff      - Ruff is fast Python check and lint for Python source code.
    vulture   - Vulture detects unused "dead" code in Python source code.

Copyright © 2025 William F. Gilreath. All Rights Reserved.

License: This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.

"""

import importlib.util
import os
import sys
from runpy import run_module
from subprocess import PIPE, run

__author__ = "William F. Gilreath"
__copyright__ = "Copyright 2025"
__credits__ = ["William F. Gilreath"]
__license__ = "GPL"
__version__ = "v3.0"
__maintainer__ = "William F. Gilreath"
__email__ = "william.f.gilreath@gmail.com"
__release__ = "v 1.3.1"

MCCABE_MIN = '3'  # mccabe cyclotomic complexity threshold for error

# required external test modules used by py7
PY_MOD_LIST = ['bandit','mccabe','mypy','pyflakes','pylint','ruff','vulture',]

def run_lint_tests(file):
    """
    Func: Function runs lint tools on Python source file.
    Args: Python source file.
    Returns: Nothing.
    """
    for py_mod in PY_MOD_LIST:

        has_file = os.path.isfile(file)
        if not has_file:
            print(":: ")
            print(f':: Error: File {file} not found; end tests!')
            print(":: ")
            return

        if py_mod == "mccabe":
            cmd = py_mod + '--min ' + MCCABE_MIN + ' ' + file
        else:
            cmd = py_mod + ' ' + file

        print("  ::>")
        print(f'  ::> {py_mod} on file: {file}')
        print("  ::>")

        result = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True,
                          shell=True, check=False)

        if len(result.stdout) == 0:
            print("  ::> ")
            print("  ::> [\nNo problems detected.", "\n  ::> ]")
            print("  ::> ")
        else:
            print("  ::> ")
            print("  ::> [\n", result.stdout, "\n  ::> ]")
            print("  ::> ")

def check_modules():
    """
    Func: The check_modules function checks, installs the lint tools.
    Args: None.
    Returns: Nothing.
    """

    print("#")
    print("# Python Linter Tool Script ", __release__)
    print("# ")
    print("# Checking for required Python modules...")
    print("#")

    for package in PY_MOD_LIST:

        print("   ")
        has_mod = importlib.util.find_spec(package)

        if has_mod:
            print(f'  #:>The {package} module exists.')
        else:
            print(f'  #:>The {package} module absent.')

            tmp_argv = sys.argv
            sys.argv = ["pip", "install"] + [ package ]

            try:
                run_module("pip", run_name="__main__")
            except SystemExit as exception:
                print("exit code: ", exception.code)
                if exception.code != 0 :
                    print(":: ")
                    print(f':: Error: The {package} module NOT installed; end tests!')
                    print(":: ")
                    sys.exit(2)

            sys.argv = tmp_argv
            print("  #:> ")
            print(f'  #:>The {package} module installed.')
            print("  #:> ")

    print("")
    input("\nPress any key to continue...\n")
    print("")

def usage():
    """
    Func: Usage function prints command-line interface parameters.
    Args: None.
    Returns: Nothing.
    """

    print("")
    print("Usage:", sys.argv[0], "{ file.py } | --help | -h")
    print("      ", sys.argv[0], "myPython.py myApp.py badCode.py")
    print("")

def version():
    """
    Func: Version function prints copyright, release version of tool.
    Args: None.
    Returns: Nothing.
    """
    print("")
    print("Py7 Lint Tool ©", __copyright__, "Release:", __release__)
    print("")

def main():
    """
    Func: Main function that runs script, lint tools.
    Args: None.
    Returns: Nothing.
    """
    print("")
    version()
    print("")

    if ("-h",'--help') in sys.argv:
        usage()
        sys.exit(0)

    if len(sys.argv) < 2:
        print(":: ")
        print(":: Error: No Python files given to check!")
        print(":: ")
        usage()
        sys.exit(1)

    check_modules()  # check for and install required modules

    print("::")
    print(":: Beginning Py7 Lint")
    print("::")
    print("   ")

    for i in range(1, len(sys.argv)):
        print("\n::--------------------------------------------------------------------------------::\n")
        run_lint_tests(sys.argv[i])
        print("   ")

    print("::")
    print(":: Completed Py7 Lint")
    print("::")

    input("\nPress any key to continue...\n")
    sys.exit(0)

if __name__ == '__main__':
    main()
