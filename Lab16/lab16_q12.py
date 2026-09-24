l=input("enter a string")
a=list(l)
b=len(a)
p=1
for i in range(b//2):
    if a[i]!=a[b-1-i]:
        p=0
        break
if p==1:
    print("its a palindrome")
else:
    print("not a palindrome")
