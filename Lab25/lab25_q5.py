import re
pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
txt=input("enter a mail id")
if re.search(pattern,txt):
    print(txt,"is a mail id")
else:
    print(txt,"is not a mail id")