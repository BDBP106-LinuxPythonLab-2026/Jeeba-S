x=int(input("give value of x axis"))
y=int(input("give value of y axis"))
if x>0 and y>0:
    print("the point lies in quadrant1")
elif x<0 and y>0:
    print("the point lies in quadrant2")
elif x<0 and y<0:
    print("the point lies in quadrant3")
elif x>0 and y<0:
    print("the point lies in quadrant4")
else:
    print("the point lies on the axis")