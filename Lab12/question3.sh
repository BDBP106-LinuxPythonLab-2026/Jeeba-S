#!/bin/bash

echo "enter a number: "
read num
i=1 
until [ $i -gt 15 ]
do
	echo "$num * $i = $((num*i))"
	i=$((i+1))
done

