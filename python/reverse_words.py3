#!/usr/bin/env python3
"""
REVERSE WORDS
CHALLENGE DESCRIPTION:
Write a program which reverses the words in an input sentence.

INPUT SAMPLE:

The first argument is a file that contains multiple sentences, one per line. 
Empty lines are also possible.

For example:
Hello World
Hello CodeEval

OUTPUT SAMPLE:
Print to stdout each sentence with the reversed words in it, one per line. 
Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces 
in each line you print.

For example:
World Hello
CodeEval Hello

"""


def  reverse_words_1(line):
	x=line.strip().split(" ")
	line=[]
	for i in range(len(x)) : line.append(x.pop())
	return " ".join(line)
	

if __name__ == '__main__':
	import sys
	test_cases = open(sys.argv[1], 'r')	
	tests=test_cases.readlines()
	test_case = 0
	MAX_TEST_CASE_NBR=40	
	try:
		for test in tests:		 
				''' The 40 TC constraint'''		
				if (test_case == MAX_TEST_CASE_NBR):
						break
				if test.strip(): #only nonempty lines are considered
					print(reverse_words_1(test))
					test_case += 1	
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)	
		
	


	
