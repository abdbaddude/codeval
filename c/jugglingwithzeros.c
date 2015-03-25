
/**
JUGGLING WITH ZEROS
CHALLENGE DESCRIPTION:

In this challenge, you will deal with zero-based numbers. A zero-based number has the following form: "flag" "sequence of zeroes" "flag" "sequence of zeroes", and so on. The numbers are separated by a single space.

00 0 0 00 00 0
You have to convert zero-based numbers into integers. To do this, you need to perform the following steps:

Convert a zero-based number into a binary form using the following rules:
a) flag "0" means that the following sequence of zeroes should be appended to a binary string.

b) flag "00" means that the following sequence of zeroes should be transformed into a sequence of ones and be appended to a binary string.

00 0 0 00 00 0 --> 1001
Convert the obtained binary string into an integer.
1001 --> 9
INPUT SAMPLE:

The first argument is a file where each line of input contains a string with zero-based number.

For example:

00 0 0 00 00 0
00 0
00 0 0 000 00 0000000 0 000
0 000000000 00 00

OUTPUT SAMPLE:

For each line of input, print an integer converted from a zero-based number.

For example:

9
1
9208
3
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>

#define LINE_SIZE 1024

#define B(x) S_to_binary_(#x)

static inline unsigned long long S_to_binary_(const char *s)
{
    unsigned long long i = 0;
    while (*s) {
        i <<= 1;
        i += *s++ - '0';
    }
    return i;
}


char* jugglingwithzeros(const char *z){
    
    return "";
}

int main(int argc, char *argv[]){
  if (argc > 1 ){
	  FILE *file = fopen(argv[1],"r");
	  char line[LINE_SIZE],*p;
	  while (fgets(line,LINE_SIZE,file)){
	  	if ((p = strchr(line, '\n'))) { *p = '\0'; } 
    	// Skip empty lines
    	if (line[0] == '\0' || line[0] == '\n') { continue; }
		jugglingwithzeros(line);
	  }
	  // Paranoid check
	  if (ferror(file)) {
		perror("I/O Error");
	  }
	  fclose(file);
	  return 0;
  } else{
  	printf("Usage: %s <input_file>\n", argv[0]);
	 return -1;
  }
}
