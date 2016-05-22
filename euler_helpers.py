from math import sqrt
from bisect import bisect_left
def sieve(n):
    primes = range(2,n)
    n_sqrt = sqrt(n)
    i = 0
    while primes[i] <= sqrt(n):
        p = primes[i]
        j = 2
        while p*j < n:
            if bin_search(primes,p*j)!=-1:
                primes.remove(p*j)
            j += 1
        i += 1

    return primes

def gcd(a,b):
    s = max(a,b)
    r = min(a,b)
    while s%r != 0:
        tmp = r
        r = s^r
        s = tmp
    return r

def bin_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a,x,lo,hi)
    return(pos if pos != hi and a[pos] == x else -1)

