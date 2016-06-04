from math import sqrt,ceil
from bisect import bisect_left
from time import time

# Optimized sieve helper function
# Input: a number to calculate all primes up to
# Output: a list of primes up to and including n
def opt_sieve(n):
    n = int(n)
    sqrt_n = int(ceil(sqrt(n)))
    primes = [True]*n
    for i in range(4,n+1,2):
        primes[i-1] = False
    for i in range(3,sqrt_n,2):
        if primes[i-1]:
            for j in range(2,int(ceil(float(n)/i))):
                primes[j*i-1] = False

    return [i+1 for i in range(1,n) if primes[i]] 

# Sieve test to check optimizations don't break it
def sieve_test():
    num_primes = [25, 168, 78498]
    return [len(opt_sieve(n)) for n in [100, 1000, 1000000]] == num_primes

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

# Generates the prime factors of n
def prime_factors(n):
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

# Finds the number of factors of n
def num_factors(n):
    pfs = sorted(prime_factors(n))
    total = 2
    count = 2
    for idx in range(1,len(pfs)):
        if pfs[idx-1]==pfs[idx]:
            count += 1
        else:
            total *= count
            count = 2
    return total

# Finds the totient (phi) of n using Euler's
# product formula
def totient(n):
    pfs = set(prime_factors(n))
    prod = n
    for p in pfs:
        prod *= (1-1.0/p)
    return prod



if __name__=='__main__':
    start = time()
    opt_sieve(1e7)
    print 'time elapsed: %.5f seconds' % (time()-start,)
    if sieve_test():
        print 'sieve test passed!'
    else:
        print 'sieve function broken...'
