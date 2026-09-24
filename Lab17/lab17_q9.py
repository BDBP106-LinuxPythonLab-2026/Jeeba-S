a=input("enter a string")
b=input("enter a string")
c=list(a)
d=list(b)
e=len(c)
f=len(d)
count=0
if e==f:
    for i in range(0,e):
            if c[i] in d:
                d.remove(c[i])
    if f==0:
        print("both strings are anagrams")
    else:
        print("both strings are not anagrams")
else:
    print("the strings are not anagram")