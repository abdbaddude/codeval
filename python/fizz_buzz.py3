#!/usr/bin/env python3
"""
FIZZ BUZZ
CHALLENGE DESCRIPTION:


Players generally sit in a circle. The first player says the number “1”, and each player 
says next number in turn. However, any number divisible by X (for example, three) is 
replaced by the word fizz, and any divisible by Y (for example, five) by the word buzz. 
Numbers divisible by both become fizz buzz. 
A player who hesitates, or makes a mistake is eliminated from the game.

Write a program that prints out the final series of numbers where those divisible by X, Y 
nd both are replaced by “F” for fizz, “B” for buzz and “FB” for fizz buzz.

INPUT SAMPLE:
Your program should accept a file as its first argument. 
The file contains multiple separated lines; each line contains 3 numbers that are space 
delimited. 
The first number is the first divider (X), 
the second number is the second divider (Y), 
and the third number is how far you should count (N). 
You may assume that the input file is formatted correctly and the numbers are valid 
positive integers.

For example:

3 5 10
2 7 15

OUTPUT SAMPLE:
Print out the series 1 through N replacing numbers divisible by X with “F”, 
numbers divisible by Y with “B” and numbers divisible by both with “FB”. 
Since the input file contains multiple sets of values, your output should print out one 
line per set. 
Ensure that there are no trailing empty spaces in each line you print.

1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15
CONSTRAINTS:

The number of test cases ≤ 20
"X" is in range [1, 20]
"Y" is in range [1, 20]
"N" is in range [21, 100]
"""

def fizz_buzz(x,y,n):
    a=n%x
    b=n%y
    if a==b and a==0 : return "FB"
    if a==0: return "F"
    if b==0: return "B"
    return n
 
def fizz_buzz2(X,Y,N): return  [fizz_buzz(X,Y,x) for x in range(1,N+1)]
 
fizz_buzz2(2,7,15)
from timeit import timeit
"""
>>> timeit('fizz_buzz2(2,7,15)','from __main__ import fizz_buzz2')
8.15096579099918
>>> timeit('fizz_buzz2(2,7,15)','from __main__ import fizz_buzz2')
8.084069682998233
"""


"""
input_tuple tuple of numbers in format (X Y N)
>>> timeit('fizz_buzz3((2,7,15))','from __main__ import fizz_buzz3')   
7.43212103843689
>>> timeit('fizz_buzz3((2,7,15))','from __main__ import fizz_buzz3')  
7.440068960189819
"""
def fizz_buzz3(input_tuple):
	X,Y,N=input_tuple
	results = []
	for n in range(1,N+1):
		word=''
		if n%X==0: 
			word='F'
		if n%Y==0: 
			word+='B'
		results.append(word)  if word != '' else results.append(n) 
	return results

"""
Eliminate attribute access results.append
Good for loops. A trick I picked up in a text.
Improves code speed  by oover 11%
input_tuple tuple of numbers in format (X Y N)
>>> timeit('fizz_buzz4((2,7,15))','from __main__ import fizz_buzz4') 
6.557060956954956
>>> timeit('fizz_buzz4((2,7,15))','from __main__ import fizz_buzz4')
6.664225101470947
>>> 
"""
def fizz_buzz4(input_tuple):
	X,Y,N=input_tuple
	results = []
	results_append = results.append
	for n in range(1,N+1):
		word=''
		if n%X==0: 
			word='F'
		if n%Y==0: 
			word+='B'
		results_append(word)  if word != '' else results_append(n) 
	return " ".join([str(i) for i in results])
  
if __name__ == '__main__':
	import sys
	test_cases = open(sys.argv[1], 'r')	
	tests=test_cases.readlines()
	test_case = 0
	MAX_TEST_CASE_NBR=20	
	try:
		for test in tests:		 
				''' The 20 TC constraint'''		
				if (test_case == MAX_TEST_CASE_NBR):
						break
				if test.strip(): #only nonempty lines are considered
					X,Y,N=test.split()
					X=int(X)
					Y=int(Y)
					N=int(N)
					if ((1<=X and X<=20) and (1<=Y and Y<=20) and (21 <= N and N <=100)): # since X,Y,N is always positive
						print(fizz_buzz4((X,Y,N)))
					test_case += 1	
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)	
