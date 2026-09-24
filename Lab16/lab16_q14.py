n=25
a=0
b=1
for i in range(n):
    c=a+b
    temp1=b
    a=temp1
    b=c
print(a,end="")