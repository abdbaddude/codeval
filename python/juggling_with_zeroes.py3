#!/usr/bin/env python3.4
""" 
JUGGLING WITH ZEROS
CHALLENGE DESCRIPTION:

In this challenge, you will deal with zero-based numbers. A zero-based number has the following form: "flag" "sequence of zeroes" "flag" "sequence of zeroes", and so on. The numbers are separated by a single space.

00 0 0 00 00 0
You have to convert zero-based numbers into integers. To do this, you need to perform the following steps:

Convert a zero-based number into a binary form using the following rules:
a) flag "0" means that the following sequence of zeroes should be appended to a binary string.

b) flag "00" means that the following sequence of zeroes should be transformed into a sequence of ones and be appended to a binary string.

00 0 0 00 00 0 --> 1001
Convert the obtained binary string into an integer.
1001 --> 9
INPUT SAMPLE:

The first argument is a file where each line of input contains a string with zero-based number.

For example:

00 0 0 00 00 0
00 0
00 0 0 000 00 0000000 0 000
0 000000000 00 00

OUTPUT SAMPLE:

For each line of input, print an integer converted from a zero-based number.

For example:

9
1
9208
3
"""

def juggle_with_zeros(zero_number):
	""" Juggle with zeroes 
	Algorithm 1
	Args:
		zero_number (string): The zero_number to convert
	Returns:
		int: the converted number
	"""
	zero_number=zero_number.split(" ")
	flags=zero_number[0::2]
	seq_zeros=zero_number[1::2]
	a=[ seq_zeros[i].replace("0","1") if flags[i] == "00" else seq_zeros[i].replace("1","0")   for i in range(len(flags))]
	return int("".join(a),2)

def juggle_with_zeros2(zero_number):
	""" Juggle with zeroes 
	Algorithm 2
	Args:
		zero_number (string): The zero_number to convert
	Returns:
		int: the converted number
	"""
	zero_number=zero_number.split(" ")
	a = []
	flags=zero_number[0::2]
	seq_zeros=zero_number[1::2]
	for i in range(len(flags)):
		a.append(seq_zeros[i].replace("0","1") if flags[i] == "00" else seq_zeros[i].replace("1","0") )
	return int("".join(a),2)

def juggle_with_zeros3(zero_number):
	""" Juggle with zeroes 
	Algorithm 3
	Args:
		zero_number (string): The zero_number to convert
	Returns:
		int: the converted number
	"""
	zero_number=zero_number.split(" ")
	a = []
	a_append=a.append #Fast trick 
	flags=zero_number[0::2]
	seq_zeros=zero_number[1::2]
	for i in range(len(flags)):
		a_append(seq_zeros[i].replace("0","1") if flags[i] == "00" else seq_zeros[i].replace("1","0") )
	return int("".join(a),2)
	
if __name__ == '__main__':
	import sys
	if(len(sys.argv) < 2):
		print("Usage : {:s} <input_file>".format(sys.argv[0]))
		sys.exit(-1)
	test_cases = open(sys.argv[1], 'r')	
	tests=test_cases.readlines()
	test_case = 0
	MAX_TEST_CASE_NBR=40	
	try:
		#from timeit import timeit
		for test in tests:		 
			''' The 40 TC constraint'''		
			if (test_case == MAX_TEST_CASE_NBR):
				break
			if test.strip(): #only nonempty lines are considered
				#print("juggle_with_zeros  {}".format(timeit('juggle_with_zeros(test)','from __main__ import juggle_with_zeros,test')))
				#print("juggle_with_zeros2 {}".format(timeit('juggle_with_zeros2(test)','from __main__ import juggle_with_zeros2,test')))
				#print("juggle_with_zeros3 {}".format(timeit('juggle_with_zeros3(test)','from __main__ import juggle_with_zeros3,test')))
				print("{}".format(juggle_with_zeros3(test)))
				test_case += 1
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)

