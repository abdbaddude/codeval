#!/usr/bin/env python

"""
Details file to be used as imput
cat >> details.txt <<EOF
XX.YY,XXX.Y,X..YY,XX..Y
XX...YY,X....YY,XX..YYY,X..YYYY
XXYY,X..Y,XX.Y
EOF
"""

def number_of_y_move(inputfile):
	"""
	DETAILS
	CHALLENGE DESCRIPTION:

	There are two details on a M*N checkered field. The detail X covers several (at least one) first cells in each line. The detail Y covers several (at least one) last cells. Each cell is either fully covered with a detail or not.

	For example:



	The detail Y starts moving left (without any turn) until it bumps into the X detail at least with one cell. Determine by how many cells the detail Y will be moved.

	INPUT SAMPLE:

	The first argument is a file with different test cases. Each test case contains a matrix the lines of which are separated by comma. (Empty cells are marked as ".")

	For example:


	1
	2
	3
	XX.YY,XXX.Y,X..YY,XX..Y
	XX...YY,X....YY,XX..YYY,X..YYYY
	XXYY,X..Y,XX.Y
	OUTPUT SAMPLE:

	Print out the number of cells the detail Y will be moved.

	For example:


	1
	2
	3
	1
	2
	0
	CONSTRAINTS:

	The matrices can be of different M*N sizes. (2 <= M <= 10, 2 <= N <= 10)
	Number of test cases is 40.
	
	"""
	test_case = 0 
	for matrix in open(inputfile,'r'):
		'''Check for nbr_rows m and nbr_col n'''
		rows=matrix.split(",")
		m = len(rows)
		if  2<=m and m <= 10:
			nbr_cells_to_move = min([row.count(".")  for row in rows if row.startswith('X') and row.endswith('Y')  and (len(row) >=2  and len(row) <= 10 )])
		print(nbr_cells_to_move)

if __name__ == '__main__':
	import sys
	if (len(sys.argv) > 1):
		try:
			number_of_y_move(sys.argv[1])
			EXIT_CODE = 0
		except:
			EXIT_CODE = -1	
	else:
		usage = 'Usage: {:s} details.txt '.format(sys.argv[0])
		print(usage)
		EXIT_CODE = -1
	sys.exit(EXIT_CODE)
		 
	