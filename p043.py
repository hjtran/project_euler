from itertools import permutations as perm


s = 0 # sum
for p in perm(range(10)):

    divs = [2,3,5,7,11,13,17]

    for i in range(len(divs)):
        if int(''.join([str(x) for x in p[i+1:i+4]])) % divs[i] != 0:
            break
    else:
        s += int(''.join([str(x) for x in p]))

print s

