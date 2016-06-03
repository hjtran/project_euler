from math import sqrt,ceil
from bisect import bisect_left
from time import time

# Optimized sieve helper function
# Input: a number to calculate all primes up to
# Output: a list of primes up to and including n
def opt_sieve(n):
    n = int(n)
    primes = [True]*n
    for i in range(4,n+1,2):
        primes[i-1] = False
    for i in range(3,int(ceil(sqrt(n))),2):
        for j in range(2,int(ceil(float(n)/i))):
            primes[j*i-1] = False

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
def prime_factors(n):
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
            pfs.append(d)
            return pfs
    pfs.append(d)
    return pfs

# Sieve test to check optimizations don't break it
def sieve_test():
    num_primes = [25, 168, 78498]
    return [len(opt_sieve(n)) for n in [100, 1000, 1000000]] == num_primes

# Generates n numbers of (p)olygonal numbers. p is the 
# num of sides of polygon (ie 3 = triangle, 4 = rectangle, etc
def polygon_range(p,n):
    p -= 2
    if p < 0:
        raise Exception('p must be greater than 2')
    s = 0
    arr = []
    for i in range(1,p*n+1,p):
        s += i
        arr.append(s)
    return arr

if __name__=='__main__':
    if sieve_test():
        print 'sieve test passed!'
    else:
        print 'sieve function broken...'
