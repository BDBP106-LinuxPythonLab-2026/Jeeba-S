#!/bin/bash

function maximum {
a=$1
b=$2

if [ $a -gt $b ]; then
	echo "$a greater than $b"
else 
	echo "$b greater than $a"
fi
}
maximum 4 2
 
