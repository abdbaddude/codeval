#!/usr/bin/env python3

"""
>>> timeit('bitpositions(86,1,2)','from __main__ import bitpositions')
0.7078518867492676
>>> timeit('bitpositions(86,1,2)','from __main__ import bitpositions')
0.7165510654449463
>>> 
def bitpositions3(n,p1,p2):
	def bit_value_of_position(position):
		return  2 << (position-2) if position > 1 else 1
    return "true" if ( (n & bit_value_of_position(p1) == bit_value_of_position(p1) ) and (n & bit_value_of_position(p2) == bit_value_of_position(p2))  ) else "false"

>>> timeit('bitpositions(86,1,2)','from __main__ import bitpositions')
0.8118760585784912
>>> timeit('bitpositions(86,1,2)','from __main__ import bitpositions')
0.8175199031829834

def bitpositions2(n,p1,p2):
    return "true" if ( (n & pow(2,p1-1) == pow(2,p1-1) ) and (n & pow(2,p2-1) == pow(2,p2-1))  ) else "false"
"""    

"""
>>> timeit('bitpositions(86,1,2)','from __main__ import bitpositions')
>>> timeit('bitpositions(86,1,2)','from __main__ import bitpositions')
0.6768369674682617
>>> timeit('bitpositions(86,1,2)','from __main__ import bitpositions')
0.7028970718383789
"""	
def bit_value_of_position(position):
	return  2 << (position-2) if position > 1 else 1
	
def bitpositions(n,p1,p2):
	p1 = 1 if n & bit_value_of_position(p1) == bit_value_of_position(p1) else 0
	p2 = 1 if n & bit_value_of_position(p2) == bit_value_of_position(p2) else 0
    return "true" if (p1 == p2) else "false"
	
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
					n,p1,p2 = [int(i) for i in test.split(",")]
					print(bitpositions(n,p1,p2))
					test_case += 1	
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)	
    