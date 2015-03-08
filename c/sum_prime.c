#include <stdio.h>
#include <math.h>

/**
Check if a number is prime
*/
int isprime(int n){
	int d =3;
	while(d <= sqrt(n) & n%d > 0 )
		d += 2;
	if(n%d == 0) return 1;
	return 0;
}

/**
Ensure you start considering 2,3 are already in the prime number list 
Next time will consider the Sieve Eratosthenes algorithm
*/
int main(int argc, char *argv[]){
 int sumofprimes = 5;
 int numberofprimes = 3;
 for (int i = numberofprimes ; numberofprimes <= 1000  ; i+= 2){
 	 if(isprime(i) == 0 ) {
 	 	sumofprimes += i;
 	 	numberofprimes++;
 	 }
  }
  printf("%i",sumofprimes);
  return 0; 
}