from euler_helpers import opt_sieve
from math import ceil,sqrt

def primeFactors(n):
    primes = opt_sieve(ceil(sqrt(n)))
    d = n
    pfs = []
    while d not in primes:
        for p in primes:
            if d%p==0:
                pfs.append(p)
                d /= p
                break
        else:
            return [n]
    pfs.append(d)
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

trinum = 1
a = 2
while numFactors(trinum) < 500:
    trinum += a
    a += 1

print trinum
