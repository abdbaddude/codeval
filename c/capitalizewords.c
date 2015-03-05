/**
CAPITALIZE WORDS
CHALLENGE DESCRIPTION:
Write a program which capitalizes the first letter of each word in a sentence.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. 
Input example is the following

Hello world
javaScript language
a letter
1st thing

OUTPUT SAMPLE:
Print capitalized words in the following way.

Hello World
JavaScript Language
A Letter
1st Thing
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define LINE_SIZE 1024



char* tails(const char* );
char* capitalizeWord(const char*);

char* capitalizeWord(const char *words){
    // You may want to remove the trailing '\n'
    char* token,word;
    char* string = strdup(words);
    assert(string != NULL);
    while ((token = strsep(&string, " ")) != NULL){
        printf("%c%s ",(('a' <= token[0]) & (token[0] <= 'z'))?token[0] - 32:token[0],tails(token));
    }
    printf("\n");
    free(string);	
    return token;
}

char* tails(const char* word){
  size_t length = strlen(word);
  char *tail = malloc(length - 1);
  for (int i = 1; i < length;i++ ) {
  	tail[i-1] = word[i];
  }
  return tail;
}

int main(int argc, char *argv[]){
  if (argc > 1 ){
	  FILE *file = fopen(argv[1],"r");
	  char line[LINE_SIZE],*p;
	  while (fgets(line,LINE_SIZE,file)){
	  	if ((p = strchr(line, '\n'))) { *p = '\0'; } 
    	// Skip empty lines
    	if (line[0] == '\0' || line[0] == '\n') { continue; }
		capitalizeWord(line);		
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


