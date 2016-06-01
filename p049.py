from euler_helpers import opt_sieve
from itertools import permutations
import time

start = time.time()

table = [ [] for i in range(10000)]

primes = opt_sieve(10000)
for p in primes:
    table[int(''.join(sorted(str(p))))].append(p)

for x in table:
    if len(x) == 3 and x[1]-x[0] == x[2]-x[1]:
        print x
    elif len(x) > 3:
        for p in permutations(x,3):
            if p[1]-p[0] == p[2]-p[1]:
                print ''.join([str(r) for r in p])

print 'script ran in %.5f seconds' % (time.time()-start,)
