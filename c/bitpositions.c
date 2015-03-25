/*
BIT POSITIONS
CHALLENGE DESCRIPTION:
Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are 
the same or not. Positions p1 and p2 are 1 based.

INPUT SAMPLE:
The first argument will be a path to a filename containing a comma separated list of 
3 integers, one list per line. E.g.

86,2,3
125,1,2

OUTPUT SAMPLE:
Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase). 
E.g.

true
false

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define LINE_SIZE 1024


int bitvalueofpositions(int*);
char* bitpositions(int,int,int);

int bitvalueofpositions(int *position){
	return  (*position > 1 ) ? 2 << (*position-2) : 1 ;
}

char* bitpositions(int n ,int p1 ,int p2){
	p1 = (n & bitvalueofpositions(&p1)) == bitvalueofpositions(&p1) ? 1 : 0;
	p2 = (n & bitvalueofpositions(&p2)) == bitvalueofpositions(&p2) ? 1 : 0;
    return (p1 == p2) ?"true" :"false";
}

int main(int argc, char *argv[]){
  if (argc > 1 ){
	  FILE *file = fopen(argv[1],"r");
	  char line[LINE_SIZE],*p;
	  char* string;
	  int n,p1,p2;
	  n=p1=p2=0;
	  
	  while (fgets(line,LINE_SIZE,file)){
	  	if ((p = strchr(line, '\n'))) { *p = '\0'; } 
    	// Skip empty lines
    	if (line[0] == '\0' || line[0] == '\n') { continue; }
        string = strdup(line);
		assert(string != NULL);
		 n = atoi(strsep(&string, ","));
		p1 = atoi(strsep(&string, ","));
		p2 = atoi(strsep(&string, ","));	
		free(string);	
		printf("%s\n",bitpositions(n,p1,p2));			 
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