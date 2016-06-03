from euler_helpers import opt_sieve
from itertools import combinations as combs

def concat(a,b):
    return a*(10**len(str(b)))+b

p_n = 1e3
primes = opt_sieve(p_n)
p_table = {}
for p in primes:
    p_table[p] = True
n = 2

pps = set() #prime pair sets
for c in combs(primes,2):
    if concat(c[0],c[1]) in p_table and concat(c[1],c[0]):
        pps.add(c)
print len(pps)
pps2 = set()
for s in pps():
    for p in primes:
        for c in combs(
