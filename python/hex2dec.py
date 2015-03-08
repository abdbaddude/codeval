#!/usr/bin/env python3


def  hex_2_dec(hex_number):
	import re
	if not re.match(r'^[0-9a-f]*$', hex_number): #All hex digit  must be in the range values 0-9a-f
		return 0
	hex_number_list = list(hex_number)
	l = len(hex_number_list)
	digits_range = range(l) 
	funcs = [lambda x, n=n: l - (1 + n)	for n in digits_range] 
	power_list = [pow(16,f(0))  for f in funcs]
	hex_number_list = [ ord(i) - 87 if re.match(r'[a-f]', i) else int(i) for i in hex_number_list]
	return sum([ power_list[i] * hex_number_list[i] for i in digits_range])


"""
3X faster than hex_2_dec due to memory management
"""
def  hex_2_dec2(hex_number):
	hex_number_list=[ord(i) - 87 if i in 'abcdef' else int(i) for i in list(hex_number)]
	i=0
	sumx=0
	while len(hex_number_list) > 0:
		sumx = sumx + (hex_number_list.pop() * pow(16,i))
		i = i + 1
	return sumx

"""
ca 1.33 X Slower than hex_2_dec2 due to memory management
"""
def  hex_2_dec3(hex_number):
	l = len(hex_number)
	hex_number_list = [ord(i) - 87 if i in 'abcdef' else int(i) for i in list(hex_number)]
	decr=lambda l=l: l - 1
	return sum([ hex_number_list[i] * pow(16,decr(l-i))  for i in [ decr(i)  for i in range(len(hex_number_list),0,-1)]])

"""
ca 1.33 X Slower than hex_2_dec2 due to memory management
"""
def  hex_2_dec4(hex_number):
	X='0123456789abcdef'
	return [ X.index(i)  for i in hex_number]
	
	    	
if __name__ == '__main__':
	import sys
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
				print(int(test.strip(),16))
				#timeit('hex_2_dec(test.strip())', 'from __main__ import hex_2_dec,test')
				#print(timeit('int(test.strip(),16)', 'from __main__ import test'))
				test_case += 1	
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)	