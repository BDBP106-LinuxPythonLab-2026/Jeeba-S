
#!/bin/bash

var1=Testing
var2=testing

if [ $var1 \> $var2 ]; then
	echo "Testing is greater than testing"
else 
	echo "testing is greater than Testing"
fi

echo $var1 $var2 >teststringfile

sort teststringfile
