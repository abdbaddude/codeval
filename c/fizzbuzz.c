/**
FIZZ BUZZ
CHALLENGE DESCRIPTION:


Players generally sit in a circle. The first player says the number “1”, and each player 
says next number in turn. However, any number divisible by X (for example, three) is 
replaced by the word fizz, and any divisible by Y (for example, five) by the word buzz. 
Numbers divisible by both become fizz buzz. 
A player who hesitates, or makes a mistake is eliminated from the game.

Write a program that prints out the final series of numbers where those divisible by X, Y 
nd both are replaced by “F” for fizz, “B” for buzz and “FB” for fizz buzz.

INPUT SAMPLE:
Your program should accept a file as its first argument. 
The file contains multiple separated lines; each line contains 3 numbers that are space 
delimited. 
The first number is the first divider (X), 
the second number is the second divider (Y), 
and the third number is how far you should count (N). 
You may assume that the input file is formatted correctly and the numbers are valid 
positive integers.

For example:

3 5 10
2 7 15

OUTPUT SAMPLE:
Print out the series 1 through N replacing numbers divisible by X with “F”, 
numbers divisible by Y with “B” and numbers divisible by both with “FB”. 
Since the input file contains multiple sets of values, your output should print out one 
line per set. 
Ensure that there are no trailing empty spaces in each line you print.

1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15
CONSTRAINTS:

The number of test cases ≤ 20
"X" is in range [1, 20]
"Y" is in range [1, 20]
"N" is in range [21, 100]
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define LINE_SIZE 1024
#define LEN 3

void fizzbuzz(int X,int Y, int N){
	char word[3]; 
	for (int n = 1 ; n < N + 1 ; n++ )	{
    	strcpy(word, "");
    	if ((n%X)==0){		
    		strcpy(word, "F");
    	}
    	if ((n%Y)==0){ 
    		strncat(word,"B",1);   			
    	}   
    	if(strncmp(word,"",1) == 0 ) 
    		printf("%i ",n);
    	else
    		printf("%s ",word); 	
    }     
    
}

int main(int argc, char *argv[]){
  if (argc > 1 ){
	  FILE *file = fopen(argv[1],"r");
	  char line[LINE_SIZE],*p,*string;
	  int X,Y,N,test_cases = 0;
	  while (fgets(line,LINE_SIZE,file)){
	  	if(test_cases>=20) {break;}
	  	if ((p = strchr(line, '\n'))) { *p = '\0'; } // Skip empty lines
    	if (line[0] == '\0' || line[0] == '\n') { continue; }  
    	string = strdup(line);
		assert(string != NULL);
		X = atoi(strsep(&string, " "));
		Y = atoi(strsep(&string, " "));
		N = atoi(strsep(&string, " "));	
		free(string);	
		if ((1<=X && X<=20) && (1<=Y && Y<=20) && (21 <= N && N <=100) ) {// since X,Y,N is always positive
			fizzbuzz(X,Y,N);
			printf("\n");
			test_cases++;
		}			
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


