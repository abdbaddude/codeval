#!/usr/bin/env python3
"""
There are two strings: A and B. Print 1 if string B occurs at the end of string A. 
Otherwise, print 0.

INPUT SAMPLE:

The first argument is a path to the input filename containing two comma-delimited strings, 
one per line. Ignore all empty lines in the input file.

For example:
1 Hello World,World
2 Hello CodeEval,CodeEval
3 San Francisco,San Jose

OUTPUT SAMPLE:

Print 1 if the second string occurs at the end of the first string. Otherwise, print 0.

For example:
1 1
2 1
3 0
"""
def trailing_or_not(source):
	list=source.strip().split(",")
	return (1 if list[1] in list[0] else 0)

import sys
test_cases = open(sys.argv[1], 'r')	
tests=test_cases.readlines()
for test in tests:
	if test.strip(): #only nonempty lines are considered
		print(trailing_or_not(test))