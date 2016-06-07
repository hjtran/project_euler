
def possSeq(x,seq):
    xs = str(x)
    seqs = str(seq)

    i = 0
    j = 0
    while j < len(seqs) and i < len(xs):
        if xs[i] == seqs[j]:
            j+=1
        i+=1
    return j ==len(seqs)

with open('inputs/p079.txt','r') as infile:
    arr = [int(x) for x in infile.readlines()]


from time import time
start = time()

solved = False
for i in range(1000,100000000):
    for seq in arr:
        if not possSeq(i,seq):
            break
    else:
        solved = True
        print i
    if solved:
        break
print 'Elapsed time: %.5f seconds' % (time()-start,) 
