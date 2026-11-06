with open('stringmatrix.dat','r+') as f:
    grid=[]
    for line in f:
        row=line.split()
        grid.append(row)
f.close()
print(grid)

row=len(grid)
col=len(grid[0])
print(row,"is the length of the row")
print(col,"is the length of the column")

for i in range(col):
    column = []
    for j in range(row):
        column.append(grid[j][i])
    print(column)
