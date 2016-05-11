
greatProd = 0

with open('inputs/p011.txt','r') as inputFile:
    grid = [ [ int(x) for x in line.split(' ') ] for line in inputFile.readlines() ]

    for i in range(len(grid)):
        for j in range(len(grid[i])-3):
            greatProd = max(greatProd,grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3])
    for i in range(len(grid)-3):
        for j in range(len(grid[i])):
            greatProd = max(greatProd,grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j])
    for i in range(len(grid)-3):
        for j in range(len(grid[i])-3):
            greatProd = max(greatProd,grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3])

print greatProd
