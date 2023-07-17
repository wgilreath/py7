# py7 or π-7 Python Code Check Linting Tool

Python py7 or "PI-seven" or π-7 lint tool combines seven Python code checking tools into one interactive tool.

The Py7 lint tool checks if the Python modules are installed in the Python environment, and if not installs the modules. The Py7 lint tool then checks the Python source files specified on the command-line. The seven tools (all open-source) are:

                bandit    - Bandit is a tool designed to find common security issues in Python source code.
                mccabe    - Check McCabe complexity in Python source code.
                mypy      - Mypy is a static type checker for Python source code.
                pyflakes  - Pyflakes checks source files for errors in Python source code.
                pylint    - Pylint analyses and checks for errors in Python source code.
                ruff      - Ruff is fast Python check and lint for Python source code.
                vulture   - Vulture detects unused "dead" code in Python source code.

# Telling You Why

My "Why?" is simple, expedience and convenience. I write Python source code daily, and wanted a tool to check and lint, a Python "spell check" but without plug-ins for an IDE, or having to install all the tools, again and again. Hence Py7, which install the tools, and then runs the interactively on Python source code. 

# License

Py7 is licensed under the GNU GPL v3. See the 'LICENSE' file in the repository for more information.

# Contact

Please feel free to contact me about Py7 at will@wfgilreath.xyz, and of course use and improve the Py7 tool! 😜

# Running Py7

Py7 was developed and runs with Python v. 3.10.10; running Py7 at the command-line is simple, give the Python files, or use the --help parameter.

```

py7.py <file1.py> <file2.py> ... <fileN.py> | --help

```

# Example with --help command-line argument

```
~>py7.py --help


Py7 Lint (C) Copyright  Copyright 2023  Release: v 1.1



Usage: py7.py { file.py } | --help
       py7.py myPython.py myApp.py badCode.py

~>

```

# Example using Py7 to check Python Files

An example of Py7 output from a check of several Python source files is:

```
~>py7.py simple_proc.py pyke.py meminfo.py none.py



Py7 Lint (C) Copyright  Copyright 2023  Release: v 1.1


#
# Python Linter Tool Script  v 1.1
# 
# Checking for required Python modules...
#
  #:>The bandit module exists.
  #:>The mccabe module exists.
  #:>The mypy module exists.
  #:>The pyflakes module exists.
  #:>The pylint module exists.
  #:>The ruff module exists.
  #:>The vulture module exists.


Press any key to continue...



::
:: Beginning Py7 Lint
::
  ::>
  ::> bandit on file: /Users/williamgilreath/simple_proc.py
  ::>
  ::> 
  ::> [
 Run started:2023-07-17 02:58:34.933877

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 8
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):
 
  ::> ]
  ::> 
  ::>
  ::> mccabe on file: /Users/williamgilreath/simple_proc.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> mypy on file: /Users/williamgilreath/simple_proc.py
  ::>
  ::> 
  ::> [
 Success: no issues found in 1 source file
 
  ::> ]
  ::> 
  ::>
  ::> pyflakes on file: /Users/williamgilreath/simple_proc.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> pylint on file: /Users/williamgilreath/simple_proc.py
  ::>
  ::> 
  ::> [
 ************* Module simple_proc
/Users/williamgilreath/simple_proc.py:1:0: C0114: Missing module docstring (missing-module-docstring)
/Users/williamgilreath/simple_proc.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)
/Users/williamgilreath/simple_proc.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
/Users/williamgilreath/simple_proc.py:11:4: C0103: Variable name "p" doesn't conform to snake_case naming style (invalid-name)

-----------------------------------
Your code has been rated at 5.00/10

 
  ::> ]
  ::> 
  ::>
  ::> ruff on file: /Users/williamgilreath/simple_proc.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> vulture on file: /Users/williamgilreath/simple_proc.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> bandit on file: /Users/williamgilreath/pyke.py
  ::>
  ::> 
  ::> [
 Run started:2023-07-17 02:58:36.756904

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: /Users/williamgilreath/pyke.py:6:0
5	import os
6	import subprocess
7	

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b603_subprocess_without_shell_equals_true.html
   Location: /Users/williamgilreath/pyke.py:39:20
38	                try:
39	                    subprocess.run(cmd.strip().split())
40	                except Exception:

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b603_subprocess_without_shell_equals_true.html
   Location: /Users/williamgilreath/pyke.py:49:12
48	        else:
49	            subprocess.run(command.split(" "))
50	    except Exception:

--------------------------------------------------

Code scanned:
	Total lines of code: 54
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 3
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 3
Files skipped (0):
 
  ::> ]
  ::> 
  ::>
  ::> mccabe on file: /Users/williamgilreath/pyke.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> mypy on file: /Users/williamgilreath/pyke.py
  ::>
  ::> 
  ::> [
 Success: no issues found in 1 source file
 
  ::> ]
  ::> 
  ::>
  ::> pyflakes on file: /Users/williamgilreath/pyke.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> pylint on file: /Users/williamgilreath/pyke.py
  ::>
  ::> 
  ::> [
 ************* Module pyke
/Users/williamgilreath/pyke.py:83:0: C0305: Trailing newlines (trailing-newlines)
/Users/williamgilreath/pyke.py:50:11: W0718: Catching too general exception Exception (broad-exception-caught)
/Users/williamgilreath/pyke.py:40:23: W0718: Catching too general exception Exception (broad-exception-caught)
/Users/williamgilreath/pyke.py:39:20: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
/Users/williamgilreath/pyke.py:41:26: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
/Users/williamgilreath/pyke.py:49:12: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
/Users/williamgilreath/pyke.py:51:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
/Users/williamgilreath/pyke.py:58:11: W0718: Catching too general exception Exception (broad-exception-caught)
/Users/williamgilreath/pyke.py:59:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
/Users/williamgilreath/pyke.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
/Users/williamgilreath/pyke.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
/Users/williamgilreath/pyke.py:71:8: R1723: Unnecessary "elif" after "break", remove the leading "el" from "elif" (no-else-break)

-----------------------------------
Your code has been rated at 7.45/10

 
  ::> ]
  ::> 
  ::>
  ::> ruff on file: /Users/williamgilreath/pyke.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> vulture on file: /Users/williamgilreath/pyke.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> bandit on file: /Users/williamgilreath/meminfo.py
  ::>
  ::> 
  ::> [
 Run started:2023-07-17 02:58:38.391937

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 38
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):
 
  ::> ]
  ::> 
  ::>
  ::> mccabe on file: /Users/williamgilreath/meminfo.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> mypy on file: /Users/williamgilreath/meminfo.py
  ::>
  ::> 
  ::> [
 /Users/williamgilreath/meminfo.py:33: error: Library stubs not installed for "psutil"  [import]
/Users/williamgilreath/meminfo.py:34: error: Library stubs not installed for "psutil._common"  [import]
/Users/williamgilreath/meminfo.py:34: note: Hint: "python3 -m pip install types-psutil"
/Users/williamgilreath/meminfo.py:34: note: (or run "mypy --install-types" to install all missing stub packages)
/Users/williamgilreath/meminfo.py:34: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 2 errors in 1 file (checked 1 source file)
 
  ::> ]
  ::> 
  ::>
  ::> pyflakes on file: /Users/williamgilreath/meminfo.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> pylint on file: /Users/williamgilreath/meminfo.py
  ::>
  ::> 
  ::> [
 ************* Module meminfo
/Users/williamgilreath/meminfo.py:53:0: C0304: Final newline missing (missing-final-newline)
/Users/williamgilreath/meminfo.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
/Users/williamgilreath/meminfo.py:37:18: C0103: Argument name "nt" doesn't conform to snake_case naming style (invalid-name)
/Users/williamgilreath/meminfo.py:42:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
/Users/williamgilreath/meminfo.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 6.67/10

 
  ::> ]
  ::> 
  ::>
  ::> ruff on file: /Users/williamgilreath/meminfo.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> vulture on file: /Users/williamgilreath/meminfo.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
:: 
:: Error: File none.py not found; end tests!
:: 
::
:: Completed Py7 Lint
::

Press any key to continue...

~>

```
