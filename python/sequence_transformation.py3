#!/usr/bin/env python3.4
"""
SEQUENCE TRANSFORMATION
CHALLENGE DESCRIPTION:

There are two sequences. The first sequence consists of digits "0" and "1", the second one 
consists of letters "A" and "B". The challenge is to determine whether it's possible to 
transform a given binary sequence into a string sequence using the following rules: 

1. "0" can be transformed into non empty sequence of letters "A" ("A", "AA", "AAA" etc.) 
2. "1" can be transformed into non empty sequence of letters "A" ("A", "AA", "AAA" etc.) 
or to non empty sequence of letters "B" ("B", "BB", "BBB" etc) e.g.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. 
Each line in this file contains a binary sequence and a sequence of letters "A" and "B" 
separated by a single whitespace. 

E.g.

1010 AAAAABBBBAAAA
00 AAAAAA
01001110 AAAABAAABBBBBBAAAAAAA
1100110 BBAABABBA

OUTPUT SAMPLE:
For each test case print out "Yes" if the transformation is possible, otherwise print "No". E.g.
Yes
Yes
Yes
No

Constraints: 
The length of a binary sequence is in range [1, 150] 
The length of a string sequence is in range [1, 1000] 
The number of test cases is <= 50
"""

"""Not Required. Fooling around"""
def make_sequence_dict(list_seq_bin,list_seq_str):
	from collections import OrderedDict
	d = OrderedDict()
	for i in range(len(list_seq_str)):
		d[list_seq_bin[i]] = [list_seq_str[i]]
	return d

"""Not Required. Fooling around"""	
def sequenceTransform(seq_xform_pair_dict):
	"""
	 e.g 
	 	list_seq_str=['AAAAABBBBAAAA','AAAAAA','AAAABAAABBBBBBAAAAAAA','BBAABABBA']
		list_seq_bin=['1010','00','01001110','1100110']
	"""
	list_seq_bin_dec=[int(i,2) for i in seq_xform_pair_dict.keys()]
	list_seq_str_dec=[int(i.replace('A','0').replace('B','1'),2)  for i in list_seq_str]
	return ["Yes" if ((list_seq_str_dec[i] &  list_seq_bin_dec[i]) == 0 ) else "No"  for i in range(len(list_seq_str_dec)) ]

"""The Real McCoy"""
def sequence_transform(seq_bin,seq_str):
	"""
	 e.g 
	 	seq_str='AAAAABBBBAAAA'
	    seq_bin='1010'
	"""
	seq_bin=int(seq_bin,2)
	seq_str=int(seq_str.replace('A','0').replace('B','1'),2)
	return "Yes" if ((seq_str &  seq_bin) == 0 ) else "No" 


if __name__ == '__main__':
	import sys
	if(len(sys.argv) < 2):
		print("Usage {:s} <input_file>",sys.argv[0])
	test_cases = open(sys.argv[1], 'r')	
	tests=test_cases.readlines()
	test_case = 0
	MAX_TEST_CASE_NBR=50	
	try:
		from timeit import timeit
		for test in tests:		 
			''' The 50 TC constraint'''		
			if (test_case == MAX_TEST_CASE_NBR):
				break
			if test.strip(): #only nonempty lines are considered
				test = test.strip().split(" ")
				"""
				The length of a binary sequence is in range [1, 150] 
				The length of a string sequence is in range [1, 1000] 
				"""
				if ((len(test[0]) in range(1,151))\
						and (len(test[1]) in range(1,1001))):
					#print("sequence_transform() ",timeit('sequence_transform(test[0],test[1])','from __main__ import  sequence_transform,test'))				
					print(sequence_transform(test[0].strip(),test[1].strip()))
					test_case += 1
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)	
	
