#!/bin/bash

if [ -e ufile ]; then
	echo " File Exist "
fi

if [ -s ufile ]; then
	echo " File is not empty"
fi

if [ -f ufile ]; then
	echo " Its a regular file"
fi

