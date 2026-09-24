l=int(input("enter a number"))
sum=0
while l>0:
    a=l%10
    sum=sum+a
    l=l//10

print(sum)
