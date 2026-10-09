from functools import reduce
a=[1,2,3,4]
result = reduce( lambda x,y: x + y, a)
print(result)

