'''#unsolved
numWaysToMake = [0]*201
#coinSizes = [1,2,5,10,20,50,100,200]
coinSizes = [1,5,10,25]

for c in coinSizes:
    numWaysToMake[c] = 1

for i in range(len(numWaysToMake)):
    for c in coinSizes:
        if i-c>0:
            numWaysToMake[i] += numWaysToMake[i-c]
        else:
            break

    

print numWaysToMake[100]'''

coinSizes = [200,100,50,20,10,5,2,1]
numCoins = [0]*len(coinSizes)
count = 0
coinSum = 200

ptr = 0
while numCoins[-1]!=sum:
    while sum([s*c for s,c in zip(coinSizes,numCoins)]) <= 200:
        if 
