from math import ceil,floor


n = 100
T = [ [0 for _ in range(n+1)] for __ in range(n+1)]

T[1][2] = 1
T[1][3] = 2

for j in range(4,n+1):
    for i in range(1,int(floor(j/2.0))+1):
        T[i][j] += 1
        for k in range(i,int(floor((j-1)/2.0))+1):
            T[i][j] += T[k][j-i]


s = 0
for k in range(n+1):
    s += T[k][n]
print(s)
import pdb; pdb.set_trace()
