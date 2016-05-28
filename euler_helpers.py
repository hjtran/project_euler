from math import sqrt
from bisect import bisect_left

# Optimized sieve helper function
# Input: a number to calculate all primes up to
# Output: a list of primes up to and including n
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

# Finds and returns the greatest common
# denominator of a and b using the euclidean 
# algorithm
def gcd(a,b):
    s = max(a,b)
    r = min(a,b)
    while s%r != 0:
        tmp = r
        r = s^r
        s = tmp
    return r

# Does a binary search for x in a, returns
# -1 if it doesn't exist, otherwise returns the
# index
def bin_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a,x,lo,hi)
    return(pos if pos != hi and a[pos] == x else -1)

# Finds the set of all prime divisors of x
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

