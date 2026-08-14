#!/bin/bash

echo "enter file name "
read filename

if [ -f $filename ]; then
       echo "file exist"
       exit 200
   
else
	echo "file doesnt exist"
	exit 201
fi

echo $?
