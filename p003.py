from math import sqrt
from bisect import bisect_left
def sieve(n):
    primes = range(2,n)
    n_sqrt = sqrt(n)
    i = 1
    while primes[i] <= n_sqrt:
        p = primes[i]
        j = 2
        while p*j < n:
            if bin_search(primes,p*j)!=-1:
                primes.remove(p*j)
            j += 1
        i += 1

    return primes

def bin_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a,x,lo,hi)
    return(pos if pos != hi and a[pos] == x else -1)


number = 600851475143
#number = 13195

p = 100
primes = sieve(p)
primeFactors = []
while number not in primes:
    for prime in primes[0:int(sqrt(number))][::-1]:
        if number%prime == 0:
            primeFactors.append(prime)
            number /= prime
            break
    else:
        p *= 2
        primes = sieve(p)

    #print number

primeFactors.append(number)

print primeFactors
