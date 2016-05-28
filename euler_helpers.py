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

def opt_sieve(n):
    primes = [True]*n
    n_sqrt = sqrt(n)
    i = 2
    while i <= sqrt(n):
        j = 2
        while i*j <= n:
            primes[i*j-1] = False
            j+=1
        i += 1

    return [i+1 for i in range(1,n) if primes[i]] 

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

def prime_divs(x):
    primes = opt_sieve(x)
    pd = set() # prime divisors
    d = x
    while d not in primes:
        for p in primes:
            if d%p==0:
                d = d/p
                pd.add(p)
                break
    pd.add(d)
    return pd

