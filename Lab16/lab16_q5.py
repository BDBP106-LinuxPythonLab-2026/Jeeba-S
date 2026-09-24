import cmath

from pyasn1_modules.rfc8018 import aes128_CBC_PAD

a=float(input("enter a number"))
b=float(input("enter another number"))
c=float(input("enter another number"))
d=b*b-4*a*c
root1=(-b+cmath.sqrt(d))/(2*a)
root2=(-b-cmath.sqrt(d))/(2*a)
print(root1)
print(root2)
