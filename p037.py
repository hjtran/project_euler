from euler_helpers import opt_sieve,bin_search
from math import log,ceil

n = 1000
tprimes = []
primes = opt_sieve(n)
i = 4

while len(tprimes) < 11:
    if i >= len(primes):
        n *= 10
        primes = opt_sieve(n)
        print 'n = %d' % (n)
    p = primes[i]
    truncations = []
    for j in range(int(ceil(log(p,10)))):
        truncations.append(p/(10**j))
        truncations.append(p%(10**(j+1)))
    if all([True if bin_search(primes,t) != -1 else False for t in truncations]):
        tprimes.append(p)
        print '%d added to tprimes' % (p)
    i+=1

print sum(tprimes)


    

