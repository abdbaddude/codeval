#include <stdio.h>
#include <math.h>


int isprime(int n){
	int d =3;
	while(d <= sqrt(n) & n%d > 0 )
		d += 2;
	if(n%d == 0) return 1;
	return 0;
}


int main(int argc, char *argv[]){
 printf("2\n3\n");
 for (int i = 3 ; i <= 10000 ; i+= 2){
 	 if(isprime(i) == 0 ) printf("%-3i\n",i);
  }
  return 0; 
}