#!/usr/bin/env python3
"""
Write a program which removes specific characters from a string.

INPUT SAMPLE:
The first argument is a path to a file. The file contains the source strings and the 
characters that need to be scrubbed. Each source string and characters you need to scrub 
are delimited by comma.

For example:
1 how are you, abc
2 hello world, def

OUTPUT SAMPLE:
Print to stdout the scrubbed strings, one per line. Ensure that there are no trailing empty spaces on each line you print.

For example:
1 how re you
2 hllo worl
"""

def remove_characters(line):
	source=line.split(",")[0].strip()
	scrub=line.split(",")[1].strip()
	return "".join([i for i in list(source) if i not in scrub]).strip()

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.strip():
    	continue
    # 'test' represents the test case, do something with it
    print(remove_characters(test))
test_cases.close()