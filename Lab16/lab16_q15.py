import math
x1=int(input("enter x coordinate for point1"))
y1=int(input("enter y coordinate for point1"))
x2=int(input("enter x coordinate for point2"))
y2=int(input("enter y coordinate for point2"))
a=x2-x1
b=a*a
c=y2-y1
d=c*c
e=b+d
distance=math.sqrt(e)
print(distance)