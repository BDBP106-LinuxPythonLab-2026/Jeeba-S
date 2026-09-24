n=int(input("Enter a number: "))
a=list(str(n))
l=len(a)
b=[]
for i in range(l):
    b.append(a[i])
    i=i-1
    print(a[i],end="")