/* --------------- NOT YET FINISHED -----------------------*/
/**
REVERSE WORDS
CHALLENGE DESCRIPTION:
Write a program which reverses the words in an input sentence.

INPUT SAMPLE:

The first argument is a file that contains multiple sentences, one per line. 
Empty lines are also possible.

For example:
Hello World
Hello CodeEval

OUTPUT SAMPLE:
Print to stdout each sentence with the reversed words in it, one per line. 
Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces 
in each line you print.

For example:
World Hello
CodeEval Hello
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define LINE_SIZE 1024


void  reverse(char*, char*);
void reverseWords(char*);


/*Function to reverse any sequence starting with pointer
  begin and ending with pointer end  */
void reverse(char *begin, char *end)
{
  char temp;
  while (begin < end)
  {
    temp = *begin;
    *begin++ = *end;
    *end-- = temp;
  }
}

void reverseWords(char *s)
{
    char *word_begin = NULL;
    char *temp = s; 
    while( *temp )
    {
        /*This condition is to make sure that the string start with
          valid character (not space) only*/
        if (( word_begin == NULL ) && (*temp != ' ') )
        {
            word_begin=temp;
        }
        if(word_begin && ((*(temp+1) == ' ') || (*(temp+1) == '\0')))
        {
            reverse(word_begin, temp);
            word_begin = NULL;
        }
        temp++;
    } 
    reverse(s, temp-1);
}

int main(int argc, char *argv[]){
  if (argc > 1 ){
	  FILE *file = fopen(argv[1],"r");
	  char line[LINE_SIZE],*p;
	  while (fgets(line,LINE_SIZE,file)){
	  	if ((p = strchr(line, '\n'))) { *p = '\0'; } 
    	// Skip empty lines
    	if (line[0] == '\0' || line[0] == '\n') { continue; }
    	char *temp = line;
    	reverseWords(line);
		printf("%s\n",line);
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


