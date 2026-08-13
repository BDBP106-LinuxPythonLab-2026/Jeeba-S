#!/bin/bash

echo "$HOME"

bcoutput=$(bc<< EOF
scale=5
3934/44343
EOF
)
echo $bcoutput

echo "The lines starting with D in the home are: " "$HOME"/D*


echo "The lines containing the username are: "
grep "$USER" /etc/passwd


