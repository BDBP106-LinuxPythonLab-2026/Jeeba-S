import string
para=("Cats love to play! Dogs love to run. Fast dogs and fast cats are both fun, but cats and dogs both love to sleep.")
p=para.lower()
l=list(p.split())
unwanted=".,!?:;"
newl=[]
for i in l:
    x=i.strip(unwanted)
    newl.append(x)
newl.sort()
print(newl)
c=[]
w=[]
count=1
for i in range(0, len(newl) - 1):
    if newl[i] == newl[i + 1]:
        count += 1


    else:
        print(newl[i],"is repeated" ,count, "times")
        w.append(newl[i])
        c.append(count)
        count = 1
print(newl[-1], "is repeated" ,count, "times")
w.append(newl[-1])
c.append(count)
print(c)
print(w)

max_count = c[0]
for count in c:
    if count > max_count:
        max_count = count
for index, count in enumerate(c):
    if count == max_count:
        print(w[index])





