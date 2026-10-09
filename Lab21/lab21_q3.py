import math
angle=(0,10,20,30)
def r(x):
    a=x*math.pi/180
    b=math.cos(a)
    c=math.sin(a)
    return b,c
result=list(map(r,angle))
print(result)
#do the lambda function



