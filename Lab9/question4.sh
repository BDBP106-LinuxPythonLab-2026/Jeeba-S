#!/bin/bash

echo $0
name=$1
age=$2
echo 'The first argument is: ' $1
echo 'The second argument is: ' $2

echo 'The number of non empty arguments are: ' $#

echo 'The list of arguments passed to the script are: ' $@

#We can store the arguments in an array by enclosing $@ in brackets
listofarguments=($@)
#recall the elements like any other array
echo ${listofarguments[1]}

echo $?

