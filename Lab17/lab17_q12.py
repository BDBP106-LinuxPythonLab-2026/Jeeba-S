a=[[9,8,7],[6,5,4]]
b=[[1,2,3],[4,5,6]]
c=[]
for i in range(2):
    row=[]
    for j in range(3):
        row.append(a[i][j]-b[i][j])
    c.append(row)
print(c)