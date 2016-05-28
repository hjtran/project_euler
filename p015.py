gridSize = 21
mat = [ [0]*gridSize for i in range(gridSize) ]
mat[gridSize-1] = [1]*gridSize
for i in range(gridSize):
    mat[i][gridSize-1] = 1

for j in range(gridSize-1)[::-1]:
    for i in range(gridSize-1)[::-1]:
        mat[i][j] = mat[i+1][j]+mat[i][j+1]
for row in mat:
    print row
