#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LINE_SIZE 1024



int mod(int,int);

int mod(int n , int m) {
	return n - m * (n/m);
}

int main(int argc, char *argv[]){
  if (argc > 1 ){
	  FILE *file = fopen(argv[1],"r");
	  char line[LINE_SIZE],*p;
	  char* token;
      char* string;
	  while (fgets(line,LINE_SIZE,file)){
	  // You may want to remove the trailing '\n'
        if ((p = strchr(line, '\n'))) { *p = '\0'; }
        // Skip empty lines
        if (line[0] == '\0') { continue; }
		string = strdup(line);
		int n = atoi(strsep(&string, ","));
		int m = atoi(strsep(&string, ","));
		free(string);		
		if (n>0 && m > 0)
		  printf("%i\n",mod(n,m));
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
