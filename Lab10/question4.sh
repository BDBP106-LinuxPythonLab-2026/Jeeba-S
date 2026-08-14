#!/bin/bash
 
echo "enter a number"
read num

if [ "$num" -ge 0 ]; then 
	if [ "$num" = 0 ]; then
		echo "its equal to 0"
	else
		echo "its positive"
	fi
else
	echo "its negative"
fi
