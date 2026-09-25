def triangle(a,b,c):
    if a+b<c or b+c<a or c+a<b:
        print("error sum of two sides should be greater than the third side")
    elif a==b==c:
        print("equilateral triangle")
    elif a!=b!=c:
        print("scalene triangle")
    else:
        print("isosceles triangle")
a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))

triangle(a,b,c)