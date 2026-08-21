#!/bin/bash

read -ra numbers < nums.txt
echo "The array elements are: " ${numbers[@]}
for n in "${numbers[@]}"
do
	echo "The double of the elements are: " $(($n*2))
done

