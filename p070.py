from euler_helpers import totient,opt_sieve
from operator import mul
from time import time 
def totient(n,pfs):
    return int(round(n*reduce(mul,[ 1-1.0/p for p in pfs ])))

n = int(1e6)

start = time()

pfs_arr = [ set() for i in range(n+1) ]

for p in opt_sieve(n):
    for i in range(p,int(n)+1,p):
        pfs_arr[i].add(p)

hits = []
for i in range(2,n):
    tot = totient(i,pfs_arr[i])
    if sorted(str(tot))==sorted(str(i)):
        hits.append( (i,tot,i/float(tot)) )
#import pdb; pdb.set_trace() 
print sorted(hits,key=lambda x:x[2])
#print min(hits,
print 'Elapsed time: %.5f seconds' % (time()-start,) 
