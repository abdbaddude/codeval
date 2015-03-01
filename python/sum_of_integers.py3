#!/usr/bin/env python3

"""
Print out the sum of integers read from a file.
INPUT SAMPLE:
The first argument to the program will be a path to a filename containing a positive integer, one per line. E.g.
5
12
OUTPUT SAMPLE:
Print out the sum of all the integers read from the file. E.g.
17
"""


if __name__ == '__main__':
	import sys
	if (len(sys.argv) > 1):
		try:
			f = open(sys.argv[1], 'rU')
			print(sum([ int(x.replace("\n","")) for x in f.readlines() ]))
			EXIT_CODE = 0
		except:
			EXIT_CODE = -1	
	else:
		usage = 'Usage: {:s} integers.txt '.format(sys.argv[0])
		print(usage)
		EXIT_CODE = -1
	sys.exit(EXIT_CODE)