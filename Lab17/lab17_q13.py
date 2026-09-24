n=[1,2,3,4,3,2,1,3,6,2,3]
k=2

for i in range(0,len(n)):
    count=0
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            count=count+1
    if count>=k and n[i] not in n[:i]:
        print(n[i])


