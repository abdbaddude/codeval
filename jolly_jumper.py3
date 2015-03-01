#!/usr/bin/env python3
"""
JOLLY JUMPERS
CHALLENGE DESCRIPTION:

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla 

A sequence of n > 0 integers is called a jolly jumper if the absolute values of the 
differences between successive elements take on all possible values 1 through n - 1. 
eg. 
1 4 2 3 
is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. 
The definition implies that any sequence of a single integer is a jolly jumper. 
Write a program to determine whether each of a number of sequences is a jolly jumper. 
INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. 
Each line in this file is one test case. 
Each test case will contain an integer n < 3000 
followed by n integers representing the sequence. The integers are space delimited.

OUTPUT SAMPLE:
For each line of input generate a line of output saying 'Jolly' or 'Not jolly'.

"""

"""
@params List of n sequence  such that 0 < n < 3000
e.g x = [1,4,2,3]
"""
def is_jolly_jumpers(seq):
	n = seq.pop(0) #first number in list is number of integers 
	if ( n == 1 and len(seq) == 1) : return True  #The definition implies that any sequence of a single integer is a jolly jumper
	else:
		if ((n == len(seq)) and (1 < n and n<3000) ): #condition must be fulfilled
			_,*tail = seq #pythonic way of removing/ignoring values
			len_tail = len(tail)
			c=[ abs(seq[i] - tail[i])  for i in range(len_tail)]
			#Decided against using sorted and used sum instead as sorted will bring in algorithm overhead of Big O = N
			#hence used sum for test
			sum_test = (sum(c)==sum(list(range(len_tail+1))))
			possible_values_test = True if (min(c) == 1 and  (n-max(c)) == 1) else False #Ensure possible values 1 .. n-1
			return possible_values_test and sum_test 
		else:
			return False

import sys
test_cases = open(sys.argv[1], 'r')	
tests=test_cases.readlines()
for test in tests:
	if test.strip(): #only nonempty lines are only considered
		s_list = test.strip().split(" ") #convert each line to a string list.
		i_list = [int(i) for i in s_list ] #convert string list to int
		print ('Jolly' if is_jolly_jumpers(i_list) else 'Not jolly' )
