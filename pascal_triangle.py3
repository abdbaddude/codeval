#!/usr/bin/env python3.4

def pascal_triangle1(depth=6):
	a=[1]
	pascal_triangle = [1]
	for d in range(0,depth):
		b=a.copy()
		b.extend([0])
		a.insert(0,0)
		a=[a[i] + b[i] for i in range(0,len(b)) ]
		pascal_triangle += a
	return pascal_triangle


def pascal_triangle2(depth=6):
	"""
	Using combination algorithms
	"""
	pascal_triangle = []
	for i in range (0,depth+1):
		coefficientList=[]	
		for j in range (0,i+1):
			coefficientList.append(combination(i,j,2))
		pascal_triangle.extend(coefficientList)
	return pascal_triangle
	

def iterative_algorithm_combination(n,k):
	"""
	Iterative implementation for solving combination 
	C(n,k) = n!/(k!)(n-k)! = (n/1)*(n-1)/2*(n-2)/3*(n-k+1)/k
	"""
	if(n<2 or k==0 or k==n) :return 1
	c=1
	for j in range (1,k+1):
		c *= (n-j+1)/j
	return int(c)

def recursive_algorithm_combination(n,k):
	"""
	Recursive implementation for solving combination 
	C(n,k) = C(n-1,k-1) + C(n-1,k) 
	"""
	if(k==0 or k==n) :return 1
	return recursive_algorithm_combination(n-1,k-1) + \
					recursive_algorithm_combination(n-1,k)
		
def combination(n,k,algorithm="iterative"):
	if algorithm == "iterative":
		return iterative_algorithm_combination(n,k)
	else:
		return recursive_algorithm_combination(n,k)

if __name__ == '__main__':
	import sys
	
	test_cases = open(sys.argv[1], 'r')	
	tests=test_cases.readlines()
	test_case = 0
	try:
		for test in tests:		 
				''' The 40 TC constraint'''		
				if (test_case == 40):
						break
				if test.strip(): #only nonempty lines are considered
					pascal_triangle = ['{:d}'.format(i) for i in pascal_triangle1(int(test))]
					print(" ".join (pascal_triangle))
					test_case += 1	
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)	