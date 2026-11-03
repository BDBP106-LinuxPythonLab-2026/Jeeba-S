import re
pattern=r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|0[0-9])$'
n=input("enter a number")
if re.fullmatch(pattern,n):
    print(n,"is a valid number")
else:
    print(n,"is not a valid number")

