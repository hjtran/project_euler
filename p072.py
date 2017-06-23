from euler_helpers import opt_sieve,prime_factors,totient
from time import time

start = time()
d = 8

rdf = 0

primes = set(opt_sieve(d))
for dd in range(2,d+1):
    if dd in primes:
        rdf += dd-1
    else:
        rdf += totient(dd)

print(rdf)
print('Time Elapsed: %.2fs' % (time()-start,))        


