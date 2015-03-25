#!/usr/bin/env python3.4





"""
def is_prime(n):
	if ( n == 1 or n == 2  or n == 3 or n == 5 ): return True
	if ( n % 2 == 0): return False
	i = 3
	import math
	j = math.sqrt(n)
	while(i <= j):
		if (n % i == 0):
			return True
		i = i + 2		
	return False
"""	

def palindrome(N):
	x=N
	rev = 0
	while (x != 0 ):
		rev = (rev * 10 ) + (x % 10)
		x = int(x/10)
	return 1 if (rev == N) else 0
	
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
    
print(max([n for  n in range (1,1000) if is_prime(n) and palindrome(n)]))
	
		
class SieveEratosthenes:
	def __init__(self,SIZE=10000):
		self.SIZE = SIZE
		self.sieve = [True]*SIZE

	@property
	def sieve(self): 
		return self.sieve
	
	# Setter function
	@sieve.setter
	def sieve(self, value):
		if not isinstance(value, list):
			raise TypeError('Expected a List') 
		self._sieve = value
		
	# Deleter function (optional)		
	@sieve.deleter
	def sieve(self):raise AttributeError("Can't delete attribute")
		 		
	def initializeSieve(self):
		for n in range(2,self.SIZE):
			if(self.sieve[n]):
				m = n
				while m * n < self.SIZE :
					self.sieve[m*n] = False
					m = m +1 
			
	def printSieve(self):
		n = 0;
		for  i in range(0,self.SIZE):
			if(self.sieve[i]):
				n = n + 1
				print("{}".format("\n" if n%10==0 else "\t") )
		println("\n {:d} primes less than {:d}".format(n, self.SIZE)); 

se = SieveEratosthenes()	
se.initializeSieve()
se.printSieve()
is_prime(27)

