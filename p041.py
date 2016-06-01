from euler_helpers import opt_sieve
from itertools import permutations
from math import ceil,sqrt
import time

primes = opt_sieve(1e6)
done = False
for p in permutations('7654321'):
    if p[-1] not in '2468':
        a = int(''.join(p))
        for p in primes[:int(ceil(sqrt(a)))]:
            if a % p == 0:
                break
        else:
            print a
            #break





