#!/usr/bin/env python3

'''
GRONSFELD CIPHER

CHALLENGE DESCRIPTION:

You are given a key and an enciphered message. 
The message was enciphered with the following vocabulary:

 !"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
Note: The first symbol is space.

Your task is to decipher the message that was enciphered with the Gronsfeld cipher using 
the given key.

The Gronsfeld cipher is a kind of the Vigenère cipher and is similar to the Caesar cipher. 
The only difference is that in the Caesar cipher, each character is shifted along by the 
same number, while in the Gronsfeld cipher, each character has its own number of shifts. 
It means that the length of key for the Gronsfeld cipher must be the same as the length of
 the message. But since it is difficult to remember such a key, especially if the message 
 is long, the key of the message is repeated until it has the same length as the message.

For example:

For the word "EXALTATION" and the key "31415", the ciphertext is the following:

E X A L T A T I O N
--------------------
3 1 4 1 5 3 1 4 1 5
			
			  |	
		  --> v
A B C D E F G H
----------------
          1 2 3    	

Accordingly, enciphered message is the following:

HYEMYDUMPS

INPUT SAMPLE:
The first argument is a file with different test cases (there are possible test cases with spaces at enciphered message). Each test case contains a key and an enciphered message separated by semicolon.
For example:

31415;HYEMYDUMPS
45162;M%muxi%dncpqftiix"
14586214;Uix!&kotvx3

OUTPUT SAMPLE:
Print to stdout a deciphered message.
For example:

EXALTATION
I love challenges!
Test input.

CONSTRAINTS:
To decode a message, use the following alphabet: " !"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
Number of test cases is 40.
'''
def initfile():
	'''
	init file with sample codes
	'''
	with open(inputfile,'wt') as f:
		print('31415;HYEMYDUMPS',file=f)
		print('14586214;Uix!&kotvx3',file=f)
		print('45162;M%muxi%dncpqftiix',file=f)

	
def gronsfeldDecipherCharacter(character,shift_number):
	"""
	Decipher the character using the gronsfeld cipher algorithm
	"""
	return chr(ord(character) - int(shift_number))
	


"""
Algorithm 1 
"""
def decipherWord(input=input):
	"""
	Decipher the word using the gronsfeld cipher algorithm
	"""
	s=[]
	key,emsg = input.split(";")
	len_key = len(key)
	len_emsg = len(emsg)
	[s.append(gronsfeldDecipherCharacter(emsg[i],key[i%len_key])) for i in range(len_emsg)]
	return ''.join(s)
	
"""
Algorithm 2 - Uses Queue  
"""
def decipherWord2(input):
	"""
	Decipher the word using the gronsfeld cipher algorithm
	"""
	s=[]
	decipher_key,word = input.split(";")
	decipher_key=[int(l) for l in list(decipher_key)] #convert all elements to int
	word=list(word)
	for letter in word:
		shift_number = decipher_key.pop(0)
		s.append(gronsfeldDecipherCharacter(letter,shift_number))
		decipher_key.append(shift_number)
	return ''.join(s)

"""
Algorithm 3 - Uses Queue  
"""
def decipherWord3(input):
	"""
	Decipher the word using the gronsfeld cipher algorithm
	"""
	s=[]
	decipher_key,word = input.split(";")
	decipher_key=[int(l) for l in list(decipher_key)] #convert all elements to int
	word=list(word)
	while len(word) > 0:
		shift_number = decipher_key.pop(0)
		s.append(gronsfeldDecipherCharacter(word.pop(0),shift_number))
		decipher_key.append(shift_number)
	return ''.join(s)
	

if __name__ == '__main__':
	import sys
	inputfile = sys.argv[1]
	try:
		test_case = 0 
		''' The 40 TC constraint'''
		import codecs
		with codecs.open(inputfile,'rU',encoding='utf-8') as f:
			for line in f:
				if (test_case == 40):
					break		
				if not line.strip() :
					continue
				print(decipherWord(line))
				test_case += 1	
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1
		
	sys.exit(EXIT_CODE)	