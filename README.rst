A tool to check the type of file

Usage:
======

check-file-type [-h] [-f FILE] [-i TYPE]

check_type -f file.json -i json

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File for which type need to check
  -i IS_TYPE, --is_type TYPE  Type of file to check


Example:
========

::

    check-file-type --file file.json --is_type json

Output:

::

    True
