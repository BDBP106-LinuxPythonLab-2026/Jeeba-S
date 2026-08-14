#!/bin/bash

echo "enter file name"
read filename

if [ -f "$filename" ]; then
		echo "file exist"
		if [ -x "$filename" ]; then
			echo "file is executable"
	else
		echo "file is not executable"
		fi
else
	echo "file doesnt exist"
fi


