a=int(input("enter the side of triangle a"))
b=int(input("enter the side of triangle b"))
c=int(input("enter the side of triangle c"))
if a==b and a==c and b==c:
    print("its a equilateral triangle")
elif a!=b or a!=c or b!=c:
    print("its a scalene triangle")
else:
    print("its a isosceles triangle")