#!/usr/bin/env python3
#
#

"""

Name: py7.py "PI-seven" or π-7

Description: This Python app uses seven Python lint tools to check Python source code. The seven tools are:

                bandit    - Bandit is a tool designed to find common security issues in Python source code.
                mccabe    - Check McCabe complexity in Python source code.
                mypy      - Mypy is a static type checker for Python source code.
                pyflakes  - Pyflakes checks source files for errors in Python source code.
                pylint    - Pylint analyses and checks for errors in Python source code.
                ruff      - Ruff is fast Python check and lint for Python source code.
                vulture   - Vulture detects unused "dead" code in Python source code.

Copyright © 2023 William F. Gilreath (will@wfgilreath.xyz) All Rights Reserved.

License: This program is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <https://www.gnu.org/licenses/>.

"""

import importlib.util
import os
import sys
import subprocess
from subprocess import PIPE, run

__author__ = "William F. Gilreath"
__copyright__ = "Copyright 2023"
__credits__ = ["William F. Gilreath"]
__license__ = "GPL"
__version__ = "v3.0"
__maintainer__ = "William F. Gilreath"
__email__ = "william.f.gilreath@gmail.com"
__release__ = "v 1.1"

MCCABE_MIN = '3'  # mccabe cyclotomic complexity threshold for error

# required external test modules used by py7
PY_MOD_LIST = ['bandit',
               'mccabe',
               'mypy',
               'pyflakes',
               'pylint',
               'ruff',
               'vulture', ]


def run_lint_tests(file):
    for py_mod in PY_MOD_LIST:

        # check if file exists
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

        result = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        result_len = len(result.stdout)

        if result_len == 0:
            print("  ::> ")
            print("  ::> [\nNo problems detected.", "\n  ::> ]")
            print("  ::> ")
        else:
            print("  ::> ")
            print("  ::> [\n", result.stdout, "\n  ::> ]")
            print("  ::> ")


def check_modules():
    print("#")
    print("# Python Linter Tool Script ", __release__)
    print("# ")
    print("# Checking for required Python modules...")
    print("#")

    for package in PY_MOD_LIST:

        has_mod = importlib.util.find_spec(package)

        if has_mod:
            print(f'  #:>The {package} module exists.')
        else:
            print(f'  #:>The {package} module absent.')

            python = sys.executable
            subprocess.check_call(
                [python, '-m', 'pip', 'install', package],
                stdout=subprocess.DEVNULL
            )

            print(f'  #:>The {package} module installed.')

    pass  # for

    print("")
    input("\nPress any key to continue...\n")
    print("")


pass  # end check_modules


def usage():
    print("")
    print("Usage:", sys.argv[0], "{ file.py } | --help")
    print("      ", sys.argv[0], "myPython.py myApp.py badCode.py")
    print("")


def version():
    print("")
    print("Py7 Lint (C) Copyright ", __copyright__, " Release:", __release__)
    print("")
    # print("Py7 Lint Written by", __author__,"(",__email__,")")
    # print("         and maintained by", __maintainer__)
    # print("")
    # print("Credits to", __credits__)
    # print("")
    # print("License:", __license__, __version__)


# check for command-line interface args
#

# print('\n')
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# print("Name of Python script:", sys.argv[0])

def main():
    # if len(sys.argv) <= 1:
    print("")
    version()
    print("")
    # sys.exit(1)

    if '--help' in sys.argv:
        usage()
        sys.exit(0)

    if len(sys.argv) < 2:
        print(":: ")
        print(":: Error: No Python files given to check!")
        print(":: ")
        usage()
        sys.exit(1)

    # else:
    #    pass
    #     n = len(sys.argv)
    #     print("\nArguments passed:")
    #     for i in range(1, n):
    #         print(sys.argv[i])
    #     print()
    pass  # end if

    check_modules()  # check for and install required modules

    print("::")
    print(":: Beginning Py7 Lint")
    print("::")

    # for i in range(1, n):
    #    print(sys.argv[i])

    # os.system('pylint main.py')

    # cmd = PY_MOD_LIST[4] + ' ' + 'main.py'

    # os.system(cmd)
    # result = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    # print("code ", result.returncode)
    # print(result.stdout)

    pass

    n = len(sys.argv)

    for i in range(1, n):
        run_lint_tests(sys.argv[i])

    print("::")
    print(":: Completed Py7 Lint")
    print("::")

    input("\nPress any key to continue...\n")

    sys.exit(0)


pass  # end main

if __name__ == '__main__':
    main()
