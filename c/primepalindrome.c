#include <stdio.h>
#include <math.h>

typedef enum { false, true } bool;

bool isprime(unsigned long);
bool ispalindrome(int);

bool ispalindrome(int n){
	int x = n;
	int reverse = 0;
	while(x != 0){
		reverse = (reverse * 10 ) + (x % 10);
		x /= 10;
	}
	return 	(reverse == n)?true:false;
}

bool isprime(unsigned long n) {
    if (n <= 3) {
        return n > 1;
    } else if (n % 2 == 0 || n % 3 == 0) {
        return false;
    } else {
        for (unsigned short i = 5; i * i <= n; i += 6) 
            if (n % i == 0 || n % (i + 2) == 0) 
                return false;
        return true;
    }
}

int main(int argc, char *argv[]){
	int maxprime = 2;
	unsigned long number=2;
	while(number <= 1000){
		if (isprime(number) && ispalindrome(number)){
			maxprime = (number > maxprime )?number:maxprime;
		}
		number++;
	}
	printf("%i",maxprime);
  	return 0;
}
    