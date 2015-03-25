/**
The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1. 
Given an integer n≥0, print out the F(n).

INPUT SAMPLE:

The first argument will be a path to a filename containing integer numbers, one per line. E.g.

5
12
OUTPUT SAMPLE:

Print to stdout, the fibonacci number, F(n). E.g.

5
144
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define LINE_SIZE 1024

long long int f(int) ;

long long int f(int n){
	if(n==0) return 0;
	if(n==1) return 1;
	return f(n-1) + f(n-2);
}

int main(int argc, char *argv[]){
  if (argc > 1 ){
	  FILE *file = fopen(argv[1],"r");
	  char line[LINE_SIZE],*p;
	  char* string;
	  int n;
	  
	  while (fgets(line,LINE_SIZE,file)){
	  	if ((p = strchr(line, '\n'))) { *p = '\0'; } 
    	// Skip empty lines
    	if (line[0] == '\0' || line[0] == '\n') { continue; }
        string = strdup(line);
		assert(string != NULL);
		 n = atoi(strsep(&string, " "));	
		free(string);	
		printf("%lli\n",f(n));			 
	  }
	  // Paranoid check
	  if (ferror(file)) {
		perror("I/O Error");
	  }
	  fclose(file);
	  return 0;
  } else{
	 return -1;
  }
}