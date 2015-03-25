#!/usr/bin/env python3.4

"""
PLAY WITH DNA
CHALLENGE DESCRIPTION:

This challenge is related to bioinformatics. To help in a DNA research, you have to write 
an algorithm that finds all the occurrences of a DNA segment in a given DNA string. 
But, it would be too easy for you. 
So, write an algorithm with the maximum N number of allowed mismatches. 
By mismatch we mean the minimum of the total number of substitutions, deletions, and insertions 
that must be performed on a DNA slice to completely match a given segment. 
You need to compare the DNA slices with the same length as a given pattern 
(for example, the segments 'AGTTATC' -> 'AGTATGC' have only 2 mismatches).

For the DNA string 'CGCCCGAATCCAG' and the segment 'CCC', 
the first match with the maximum 1 allowed mismatch is 'CGC', 
the second one is 'GCC', 
the third one is 'CCC', and so on.

CCC -> CGC # One mismatch
CCC -> GCC # One mismatch
CCC -> CCC # 0 mismatch

For the given segment 'CCC', the DNA string 'CGCCCGAATCCAG', and the maximum 
allowed mismatch '1', the list of the matches is 'CGC GCC CCC CCG TCC CCA'.

INPUT SAMPLE:

Your program should accept a path to a filename as its first argument. 
Each line in the file contains a segment of DNA, the maximum number of allowed mismatches N, 
and a DNA string separated by a single space.

CCC 1 CGCCCGAATCCAG
GCGAG 2 CCACGGCCTATGTATTTGCAAGGATCTGGGCCAGCTAAATCAGCACCCCTGGAACGGCAAGGTTCATTTTGTTGCGCGCATAG
CGGCGCC 1 ACCCCCGCAGCCATATGTCCCCAGCTATTTAATGAGGGCCCCGAACACGGGGAGTCTTACACGATCTGCCCTGGAATCGC

OUTPUT SAMPLE:

Print out all the occurrences of a segment S in a DNA string in the order from the best 
match (separated by a single space) taking into account the number of allowed mismatches. 
In case of several segments with the equal number of matches, print them in alphabetical 
order. If there is no such a case, print out 'No match'.

CCC CCA CCG CGC GCC TCC
GCAAG GCAAG GCCAG GCGCG GCGCA GCTAA
No match

CONSTRAINTS:

The length of a DNA string is in a range from 100 to 300.
N is in a range from 0 to 40.
The length of a segment S is in a range from 3 to 50.
"""

def is_segment_match(dna_slice,segment,segment_len=0):
	""" Is DNA slice and segment a mismatch
	Args:
		dna_slice (string): The DNS string slice 
		segment (string): The segment S used for pattern matching
		segment_len (int): Optional.Defaults to 0
			The length of segment
	
	Returns:
		int: Number of mismatches 
	"""
	if segment_len == 0 : segment_len = len(segment)
	mismatch_cnt=0
	for n in range(segment_len):
		 if dna_slice[n] != segment[n]: mismatch_cnt += 1
	return mismatch_cnt


def get_match_dna_slices(S=None,N=0,DNA=None):
	""" Get matching DNA Slices
	Args:
		S (string): The segment S used for pattern matching.Default None
		N (int): Optional.Defaults to 0
			The allowed number of mis maches
		DNA (string): The DNS string to be examined.Default None
	Returns:
		string: String of matched slices seperated by " " 
	"""
	if (S is None or  DNA is None): return "No match"
	dna_len=len(DNA)
	S_len=len(S)
	dna_slice_dict = dict()
	for i in range(dna_len-S_len+1):
		dna_slice = DNA[i:i+S_len] #compare the DNA slices with the same length as a given pattern 
		mismatch_cnt=is_segment_match(dna_slice,S,S_len)
		if (mismatch_cnt <= N):
			dna_slice_dict[dna_slice] = mismatch_cnt
	dna_slice_list = sorted(zip(dna_slice_dict.values(), dna_slice_dict.keys()))
	return " ".join([i[1] for i in dna_slice_list]) if len(dna_slice_list) > 0 else "No match"


if __name__ == '__main__':
	import sys
	if(len(sys.argv) < 2):
		print("Usage {:s} <input_file>",sys.argv[0])
	test_cases = open(sys.argv[1], 'r')	
	tests=test_cases.readlines()
	test_case = 0
	#MAX_TEST_CASE_NBR=40	
	try:
		#from timeit import timeit
		for test in tests:		 
			''' The 40 TC constraint'''		
			#if (test_case == MAX_TEST_CASE_NBR):
				#break
			if test.strip(): #only nonempty lines are considered
				S,N,DNA = test.strip().split(" ")
				N=int(N) #Ensure it is an integer
				#print(timeit('get_match_dna_slices(S,N,DNA)','from __main__ import get_match_dna_slices,S,N,DNA'))
				DNA_len = len(DNA)
				S_len = len(S)
				if ((100 <= DNA_len  and DNA_len <= 300)\
				and (0 <= N and N <= 40) \
				and (3 <= S_len and S_len <= 52)):
					print(get_match_dna_slices(S,N,DNA))
					#test_case += 1
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)