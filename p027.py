from euler_helpers import opt_sieve, bin_search

primes = opt_sieve(1000000)
maxa = None
maxb = None
maxCount = 0
for a in range(-999,1000):
    for b in range(-999,1000):
        n = 0
        count = 0
        while bin_search(primes,n**2+a*n+b) != -1:
            count += 1
            n += 1
            if count > maxCount:
                maxa = a
                maxb = b
                maxCount = count

print maxa*maxb
