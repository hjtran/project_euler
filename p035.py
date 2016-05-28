from euler_helpers import opt_sieve, bin_search

n = int(1e6)

primes = opt_sieve(n)
count = 0
for p in primes:
    rotations = []
    str_p = str(p)
    for i in range(len(str_p)):
        rotations.append(int(str_p[i:]+str_p[:i]))
    if sum([1 for r in rotations if bin_search(primes,r)!=-1])==len(rotations):
        print p
        count += 1
print count
