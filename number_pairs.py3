#!/usr/bin/env python3

"""
You are given a sorted array of positive integers and a number 'X'. Print out all pairs of numbers whose sum is equal to X. Print out only unique pairs and the pairs should be in ascending order

INPUT SAMPLE:

Your program should accept as its first argument a filename. This file will contain a comma separated list of sorted numbers and then the sum 'X', separated by semicolon. Ignore all empty lines. If no pair exists, print the string NULL e.g.

1,2,3,4,6;5
2,4,5,6,9,11,15;20
1,2,3,4;50
OUTPUT SAMPLE:

Print out the pairs of numbers that equal to the sum X. The pairs should themselves be printed in sorted order i.e the first number of each pair should be in ascending order. E.g.

1,4;2,3
5,15;9,11
NULL
"""


"""
Number pairing
"""
def number_pairing(numbersStr):
	sumX=int(numbersStr.split(";")[1])
	numbers=numbersStr.split(";")[0].split(",")
	consider = [ int(i) for i in numbers if ( int(i) <= sumX )] #Remove numbers greater than the sum
	sumXpairs = []
	while len(consider) > 0:
		print(consider)
		head,*tail=consider
		if sumX-head in consider:
			pair = []
			pair.append(head)
			pair.append(sumX-head)
			consider.remove(head)
			consider.remove(sumX-head)
			if pair not in sumXpairs:
				sumXpairs.append(pair)
		else:
			consider = tail	
	return sumXpairs


if __name__ == '__main__':
	import sys
	if (len(sys.argv) > 1):
		try:
			for line in open(sys.argv[1],'r'):
				if not line.strip() :  #ignore empty lines
					continue			
				list=number_pairing(line.strip())
				list=";".join([ ",".join([ str(halofpair) for halofpair in pair ]) for pair in list])
				if len(list) > 1: 
					print(list)
				else:
					print("NULL")			
			EXIT_CODE = 0
		except:
			EXIT_CODE = -1	
	else:
		usage = 'Usage: {:s} some_file_containing_integer.txt '.format(sys.argv[0])
		print(usage)
		EXIT_CODE = -1
	sys.exit(EXIT_CODE)