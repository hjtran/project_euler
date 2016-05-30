from euler_helpers import opt_sieve, bin_search

primes = opt_sieve(int(100))

cp = 2 # number of consec primes
p = 0

i = 0
while i < len(primes)-cp:

    # if sum is a prime
    s = sum(primes[i:i+cp])
    if bin_search(primes,s)!=-1:
        p = s if s < 100 else p
        cp += 1
    else:
        i += 1
print p
