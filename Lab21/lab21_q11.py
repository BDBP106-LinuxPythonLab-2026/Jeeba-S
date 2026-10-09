from functools import reduce
s1="Hi"
s2="im"
s3="Jeeba"
l1=list(s1.split())
l2=list(s2.split())
l3=list(s3.split())
l1.extend(l2)
l1.extend(l3)
print(l1)
l=reduce(lambda x,y: x+' '+y,l1)
print(l)
