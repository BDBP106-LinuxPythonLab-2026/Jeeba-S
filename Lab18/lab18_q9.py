n=int(input("enter the start position"))
seq="AGTCTTATATCT"
i=n-1
j=n
k=n+1
while k<len(seq):
    print(seq[i]+seq[j]+seq[k])
    i=i+3
    j=j+3
    k=k+3
