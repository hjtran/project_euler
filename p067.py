
with open('inputs/p067.txt') as inputfile:
    triangle = [ [ int(x) for x in line.split(' ') ] for line in inputfile.readlines() ]
    maxPath = [ [ 0 for element in row] for row in triangle]

maxPath[0][0] = triangle[0][0]

for i in range(1,len(maxPath)):
    for j in range(len(maxPath[i])):
        if j==0:
            maxPath[i][j] = triangle[i][j]+maxPath[i-1][j]
        elif j==len(maxPath[i])-1:
            maxPath[i][j] = triangle[i][j]+maxPath[i-1][j-1]
        else:
            maxPath[i][j] = triangle[i][j]+max(maxPath[i-1][j-1],maxPath[i-1][j])

print max(maxPath[-1])
