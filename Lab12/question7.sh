#!/bin/bash

function dir {
	echo "enter a filename: "
	read directory
	if [ -e $directory ];then
		echo "Directory exist"
		ls $directory  
	else 
		mkdir newdirectory
		echo " new directory made "
	fi
}
dir
