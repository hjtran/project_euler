from euler_helpers import opt_sieve
from itertools import combinations as comb
primes = opt_sieve(1e6)
hits = {}
n = 8
for p in primes:
    ps = str(p)
    for d in range(10):
        ds = str(d)
        dig_idxs = [idx for idx in range(len(ps)) if ps[idx]==ds]
        for d_count in range(1,ps.count(ds)+1):
            combs = comb(dig_idxs,d_count)
            for c in combs:
                x_ps = list(ps)
                for idx in c:
                    x_ps[idx] = '*'
                x_ps = ''.join(x_ps)
                if x_ps not in hits:
                    hits[x_ps] = set([ps])
                else:
                    hits[x_ps].add(ps)
                    if len(hits[x_ps]) == n:
                        print x_ps,sorted(list(hits[x_ps]))
