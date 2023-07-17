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

Please feel free to contact me about Py7 at will@wfgilreath.xyz, and of course improve the tool! 😜

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
  ::> bandit on file: py7.py
  ::>
  ::> 
  ::> [
 Run started:2023-06-30 12:44:19.170222

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: py7.py:37:0
36	import sys
37	import subprocess
38	from subprocess import PIPE, run

--------------------------------------------------
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: py7.py:38:0
37	import subprocess
38	from subprocess import PIPE, run
39	

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: py7.py:81:17
80	
81	        result = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
82	        result_len = len(result.stdout)

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b603_subprocess_without_shell_equals_true.html
   Location: py7.py:111:12
110	            python = sys.executable
111	            subprocess.check_call(
112	                [python, '-m', 'pip', 'install', package],
113	                stdout=subprocess.DEVNULL
114	            )
115	

--------------------------------------------------

Code scanned:
	Total lines of code: 127
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 3
		Medium: 0
		High: 1
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 4
Files skipped (0):
 
  ::> ]
  ::> 
  ::>
  ::> mccabe on file: py7.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> mypy on file: py7.py
  ::>
  ::> 
  ::> [
 Success: no issues found in 1 source file
 
  ::> ]
  ::> 
  ::>
  ::> pyflakes on file: py7.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
  ::>
  ::> pylint on file: py7.py
  ::>
  ::> 
  ::> [
 ************* Module py7
py7.py:9:0: C0301: Line too long (107/100) (line-too-long)
py7.py:11:0: C0301: Line too long (107/100) (line-too-long)
py7.py:21:0: C0301: Line too long (103/100) (line-too-long)
py7.py:22:0: C0301: Line too long (105/100) (line-too-long)
py7.py:25:0: C0301: Line too long (114/100) (line-too-long)
py7.py:26:0: C0301: Line too long (117/100) (line-too-long)
py7.py:61:0: C0116: Missing function or method docstring (missing-function-docstring)
py7.py:81:17: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
py7.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
py7.py:118:4: W0107: Unnecessary pass statement (unnecessary-pass)
py7.py:124:0: W0107: Unnecessary pass statement (unnecessary-pass)
py7.py:126:0: C0116: Missing function or method docstring (missing-function-docstring)
py7.py:132:0: C0116: Missing function or method docstring (missing-function-docstring)
py7.py:152:0: C0116: Missing function or method docstring (missing-function-docstring)
py7.py:177:4: W0107: Unnecessary pass statement (unnecessary-pass)
py7.py:197:4: W0107: Unnecessary pass statement (unnecessary-pass)
py7.py:199:4: C0103: Variable name "n" doesn't conform to snake_case naming style (invalid-name)
py7.py:213:0: W0107: Unnecessary pass statement (unnecessary-pass)

------------------------------------------------------------------
Your code has been rated at 8.12/10 (previous run: 8.12/10, +0.00)

 
  ::> ]
  ::> 
  ::>
  ::> ruff on file: py7.py
  ::>
  ::> 
  ::> [
 py7.py:9:89: E501 Line too long (107 > 88 characters)
py7.py:11:89: E501 Line too long (107 > 88 characters)
py7.py:14:89: E501 Line too long (90 > 88 characters)
py7.py:21:89: E501 Line too long (103 > 88 characters)
py7.py:22:89: E501 Line too long (105 > 88 characters)
py7.py:25:89: E501 Line too long (114 > 88 characters)
py7.py:26:89: E501 Line too long (117 > 88 characters)
py7.py:28:89: E501 Line too long (90 > 88 characters)
Found 8 errors.
 
  ::> ]
  ::> 
  ::>
  ::> vulture on file: py7.py
  ::>
  ::> 
  ::> [
No problems detected. 
  ::> ]
  ::> 
::
:: Completed Py7 Lint
::

Press any key to continue...


~>
```
