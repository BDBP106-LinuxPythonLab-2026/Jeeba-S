#!/bin/bash

function divide {
	local num1=$1
	local num2=$2
	if [ $num2 -eq 0 ]; then
		echo " Division by 0 is not allowed "
		return
	fi
		local quotient=$(echo "scale=2 ; $num1 / $num2"| bc)
		local remainder=$(echo "scale=2 ; $num1 % $num2"| bc)
		echo "The quotient is: $quotient"
                echo "The remainder is : $remainder"
 }
divide 4 2
divide 4 0
