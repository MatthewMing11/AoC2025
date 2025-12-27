# Python script for day 4
file = open("input.txt","r")
total = 0
grid=file.readlines()
grid=[i.strip() for i in grid]
row=len(grid)
col=len(grid[0])
def neighbors(grid,i,j,row,col):
    total=0
    if i>0:
        if grid[i-1][j]=='@':
            total+=1
        if j>0:
            if grid[i-1][j-1]=='@':
                total+=1
        if j<col-1:
            if grid[i-1][j+1]=='@':
                total+=1
    if j>0:
        if grid[i][j-1]=='@':
            total+=1
    if i<row-1:
        if grid[i+1][j]=='@':
            total+=1
        if j>0:
            if grid[i+1][j-1]=='@':
                total+=1
        if j<col-1:
            if grid[i+1][j+1]=='@':
                total+=1
    if j<col-1:
        if grid[i][j+1]=='@':
            total+=1
    return total

for i in range(row):
    for j in range(col):
        if grid[i][j]=='@' and neighbors(grid,i,j,row,col)<4:
            total+=1
print(total)

#part 2
file = open("input.txt","r")
grid=file.readlines()
grid=[i.strip() for i in grid]
row=len(grid)
col=len(grid[0])
grid=[list(i) for i in grid]
grandtotal=0
while True:
    total=0
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='@' and neighbors(grid,i,j,row,col)<4:
                grid[i][j]='.'
                total+=1
    print(grid)
    grandtotal+=total
    if total==0:
        break
print(grandtotal)