#!/bin/bash

echo " enter a number "
read num

if [ "$num" -lt 70 ]; then
	echo "FAILED"
else
	if [ "$num" -ge 70 ] && [ "$num" -lt 80 ]; then
		echo "The grade value is C"
	else
		if [ "$num" -ge 80 ] && [ "$num" -lt 90 ]; then
			echo  "The grade value is B"
		else
			echo " The garde value is A"
		fi
	fi
fi
