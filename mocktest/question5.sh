#!/bin/bash

var1=$1
var2=$2
var3=$3
var4=$4
echo "The number of arguments given are: " $#
if [ $# -lt 4 ]; then
	echo " Less than 4 arguments cant proceed "
	exitcode=1
	echo "The exit code is "$exitcode
else
	echo "First argument is: "$var1
	echo "Second argument is: "$var2
	echo "Third argument is: "$var3
	echo "Fourth argument is: "$var4
	echo "The exit code is "$?
fi

