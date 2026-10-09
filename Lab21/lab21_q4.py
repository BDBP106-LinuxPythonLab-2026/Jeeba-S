n=int(input("enter a number the fibonacci series will take"))
l=[]
first=0
sec=1
x=first+sec
l.append(first)
l.append(sec)
l.append(x)
while len(l)<n:
    first=sec
    sec=x
    x=first+sec
    l.append(x)
print(l)

def f(x):
    return x%2!=0
result=list(filter(f,l))
print(result)
