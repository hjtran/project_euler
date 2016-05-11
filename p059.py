
with open('inputs/p059.txt','r') as infile:
    cipher = [int(x) for x in infile.readline().split(',')]
    
    maxe = (0, [0,0,0])
    for k1 in range(61,123):
        for k2 in range(61,123):
            for k3 in range(61,123):
                ecount = 0
                i = 0
                while i+2 < len(cipher):
                    if cipher[i] ^ k1 == 101:
                        ecount += 1
                    elif cipher[i+1] ^ k2 == 101:
                        ecount += 1
                    elif cipher[i+2] ^ k3 == 101:
                        ecount += 1
                    i += 3

                if ecount > maxe[0]:
                    maxe = (ecount, [k1, k2, k3])


print maxe
print sum([maxe[1][i%3]^cipher[i] for i in range(len(cipher))])
