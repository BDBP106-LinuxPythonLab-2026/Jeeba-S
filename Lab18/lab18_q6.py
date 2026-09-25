import math
def triangle(a,b,c):

    if a+b<c or b+c<a or c+a<b:
        print("error sum of two sides should be greater than the third side")
    else:
        t = a + b + c
        s = t / 2
        d1 = s - a
        d2 = s - b
        d3 = s - c
        m = s * d1 * d2 * d3
        area = math.sqrt(m)
        print(area)
a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
triangle(a,b,c)


