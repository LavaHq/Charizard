#!/usr/bin/env python
# pylint: disable=anomalous-backslash-in-string
'''Calls pylint with a special set of parameters.'''
import os
import re
import sys

from pylint.reporters.text import TextReporter
from cStringIO import StringIO
sys.path.append('/var/charizard/src')

# check if pylint is installed and import it
try:
    from pylint import lint
except ImportError:
    print "Can't import module pylint. Did you install it?"
    sys.exit(-1)

# either use the files given on the command line or all '*.py' files
# located in and beyond the working directory
FILES = []

# pylint: disable=invalid-name
argc = len(sys.argv)
list_flag = False

if argc > 1:
    if sys.argv[1] == 'list':
        list_flag = True
    else:
        FILES = sys.argv[1:argc]

if list_flag or argc <= 1:
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        FILES.extend(
            os.path.join(dirpath, filename)
            for filename in filenames
            if ".py" == filename[-3:]
        )

# A list of messages that should not be printed by pylint.
SUPRESSED_MESSAGES = [
]

pylint_output = StringIO()
pylint_reporter = TextReporter(output=pylint_output)

PARAMS = [
    '--reports=n',
    '--disable=%s' % ",".join(SUPRESSED_MESSAGES),
    '--dummy-variables-rgx=%s' % "_$|dummy|unused"
]
PARAMS.extend(FILES)


if list_flag:
    lint.Run(PARAMS, reporter=pylint_reporter, exit=False)
    linted_files = set([])
    module_pattern = re.compile('[\*]{13}[\s]Module[\s](.+)')
    result = re.findall(module_pattern, pylint_output.getvalue())
    for module in result:
        linted_files = linted_files | set([module])
    if linted_files:
        print 'Lint Covered Files:'
    else:
        print 'All files are Dry-Cleaned, Ironed, and Linted'
    for module in linted_files:
        print '\t%s' % module
    print ''
else:
    for file_ in FILES:
        os.system('pep8 %s' % (file_,))
    lint.Run(PARAMS)
