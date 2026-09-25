a=[23,32,33,44,"BDBH101","hello","python", 15, 1e-10, True,"hit"]
print("before swapping",a)
for i in range(0,len(a)-1,2):
    a[i],a[i+1]=a[i+1],a[i]

print("after swapping",a)