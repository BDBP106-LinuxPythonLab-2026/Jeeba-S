#!/bin/bash

for i in {0..50}
do
	if [ $((i % 2)) == 0 ]; then
		echo "$i"
	fi
done
