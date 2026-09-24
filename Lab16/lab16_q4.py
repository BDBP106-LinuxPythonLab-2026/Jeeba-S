import math
angle=float(input("Enter the angle in degrees: "))
radian=angle*math.pi/180
sin=math.sin(radian)
cos=math.cos(radian)
tan=math.tan(radian)
cosec=1/sin
sec=1/cos
cot=1/tan
print(sin,cos,tan,cosec,sec,cot)