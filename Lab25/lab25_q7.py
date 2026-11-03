import re
pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
text=input("enter text")
email=re.findall(pattern,text)
unique_mail=[]
for i in email:
    if i not in unique_mail:
        unique_mail.append(i)
print("unique email address are")
for i in unique_mail:
    print(i)
