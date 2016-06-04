with open('inputs/p081.txt','r') as infile:

    matrix = []
    for line in infile.readlines():
        matrix.append( [int(c) for c in line.split(',')] )


dp = [ [0]*len(matrix[0]) for i in range(len(matrix)) ]
dp[0][0] = matrix[0][0]

for c in range(len(matrix)):
    for r in range(len(matrix)):
        poss = []
        if r>0:
            poss.append(dp[r-1][c])
        if c>0:
            poss.append(dp[r][c-1])
        if poss == []:
            poss = [0]
        dp[r][c] = matrix[r][c] + min(poss)
print dp[-1][-1]
