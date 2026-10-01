#long form
#a=[]
#for i in range(1,51):
#   a.append(i)
#print(a)
from jinja2.ext import do

#comprehension
a=[i for i in range (1,51)]
print(a)

print("slice with positive step")
print("part a", a[1:5])
print("part b", a[3:20:2])
print("part c", a[::2])
print("part d", a[::])
print("part e", a[10::2])
print("part f", a[1:1:1])
print("part g", a[:0:])
print("part h", a[-7::1])
print("part i", a[-6:])
print("part j", a[-10:-4])

print("slice with negative step")
print("part a", a[::-1])
print("part b", a[::-3])
print("part c", a[:1:-2])
print("part d", a[-1:-1:-1])
print("part e", a[:-5:-1])
print("part f", a[:0:-1])
print("part g", a[:-1:-1])
print("part h", a[0:-5:-1])
print("part i", a[-1:5:-1])
print("part j", a[2:2:-1])
print("part k", a[2:1:-1])
print("part l", a[0:-5])


print("even numbers", a[1::2])

b=a[0:10]
b.extend(a[35:50:2])
print("the new empty list contaning first 10 elemenents and even numbers from 35 to 50" , b)

#question2
#parta
total=0
i=0
while i<len(a):
    total=total+a[i]
    i=i+1
print("the sum of all the elements is" , total)

e=len(a)
sumation=sum(a[i] for i in range (e))
print("sum of elements using comprehension", sumation)

#partb
d=[x for x in range (e)  if x>1 and all(x%i!=0 for i in range (2,x))]
print("the prime numbers are" , d)

#partc
c=[]
i=0
while i<e:
    if a[i] in b:
        c.append(a[i])
    i=i+1
print("the common numbers are" , c)

#question3
#partI
#parta
g=",".join (str(x) for x in a)
print("separated by ,: " , g)
#partb
h=".".join (str(x) for x in a)
print("separated by .: " , h)
#partc
i="-".join (str(x) for x in a)
print("separated by -: " , i)
#partd
j="\n".join (str(x)+" "+str(x*x)for x in a)
print(j)

#partII
#parta
name=["jayasri su","jeeba s","adithi joshi","adhyasha patnayak","vikas kumar","prachi dalia","isha c","priyanshi rajput","mary saj","shilo paul"]
k=[x.upper() for x in name]
print(k)
#partb
l=[' '.join([name.split( )[1],name.split( )[0]]) for name in name]
print(l)
#partc
m=[name.split( )[0].capitalize()+"."+name.split( )[1].capitalize() for name in name]
print(m)

#partIII
n=["She sells sea shells that she collects from the sea floor"]
o=[max(n.split(),key=len) for n in n]
print(o)

#partIV
q="She sells sea shells that she collects from the sea floor"
p=[word for word in set(q.lower().split()) if q.lower().split().count(word) > 1]
print(p)


