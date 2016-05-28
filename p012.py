from euler_helpers import opt_sieve
from math import ceil,sqrt
trinum = 28
i = 7

prime_factors = []
while len(prime_factors) < 500:
    i += 1
    trinum += i
    primes = opt_sieve(int(ceil(sqrt(trinum))))
    prime_factors = set()
    prime_factors.add(1)
    prime_factors.add(trinum)

    for prime in primes:
        if trinum%prime==0:
            prime_factors.add(prime)
            prime_factors.add(trinum/prime)
    print len(prime_factors)

print trinum
