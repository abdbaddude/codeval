#!/usr/bin/env python3.4

"""
LOWERCASE
CHALLENGE DESCRIPTION:
Given a string write a program to convert it into lowercase.

INPUT SAMPLE:
The first argument will be a path to a filename containing sentences, one per line. 
You can assume all characters are from the english language. 
E.g.
HELLO CODEEVAL
This is some text

OUTPUT SAMPLE:
Print to stdout, the lowercase version of the sentence, each on a new line. 
E.g.
hello codeeval
this is some text
"""


def lower_case1(sentence):
	return "".join([ chr(ord(i) + 32)if (65 <= ord(i) and ord(i) <=90) else i  for i in sentence]);

def lower_case(sentence):
	lower_sentence = list()
	lower_sentence_append=lower_sentence.append
	for i in sentence:
		n = ord(i)	
		if (65 <= n and n <=90):
			lower_sentence_append(chr(n + 32))
		else:
			lower_sentence_append(i)
	return "".join(lower_sentence)

def lower_case2(sentence):
	lower_sentence = ""
	for i in sentence:
		n = ord(i)	
		if (65 <= n and n <=90):
			lower_sentence += chr(n + 32)
		else:
			lower_sentence += i
	return lower_sentence 


			
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
				test = test.strip()
				print("lower_case2() ",timeit('lower_case2(test)','from __main__ import  lower_case2,test'))	
				print("lower_case1() ",timeit('lower_case1(test)','from __main__ import  lower_case1,test'))					
				print("lower_case() ",timeit('lower_case(test)','from __main__ import  lower_case,test'))	
				print("lower() ",timeit('test.lower()','from __main__ import test'))				
				#print(lower_case(test))
				test_case += 1
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)	
