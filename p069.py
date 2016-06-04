from fractions import gcd
from euler_helpers import opt_sieve
from math import ceil,sqrt
from time import time

primes = opt_sieve(ceil(sqrt(1000000)))
ptable = set(primes)
def primeFactors(n):
    if n == 0:
        raise Exception('cant factorize 0')
    d = n
    pfs = []
    while d%2 == 0:
        pfs.append(2)
        d /= 2
    for i in range(3,int(ceil(sqrt(n)))+2):
        if d%i == 0:
            while d%i == 0:
                pfs.append(i)
                d /= i
    if len(pfs)==0:
        return [n]
    else:
        return pfs

def numFactors(n):
    pfs = sorted(primeFactors(n))
    total = 2
    count = 2
    for idx in range(1,len(pfs)):
        if pfs[idx-1]==pfs[idx]:
            count += 1
        else:
            total *= count
            count = 2
    return total

def totient(n):
    pfs = set(primeFactors(n))
    prod = n
    for p in pfs:
        prod *= (1-1.0/p)
    return prod

start = time() 

n = 1000000
#n = 10
m = 0
a = 0
primes = set(opt_sieve(n))
for i in range(2,n+1):
    tot = totient(i)
    if i/tot > m:
        m = i/tot
        a = i
print a

print 'Elapsed time: %.5f seconds' % (time()-start,) 
