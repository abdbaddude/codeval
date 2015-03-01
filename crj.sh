#
#@author abdbadddude abd_adebiyi@yahoo.com
# $description 
#   Compile and Run java codes 
# $history 
#   2015-MAR-01 Draft including parsing a line argument(s) to the program   
#
javac ${1}.java -d classes/
export CLASSPATH=./classes:$CLASSPATH
java ${1} ${2} ${3}
