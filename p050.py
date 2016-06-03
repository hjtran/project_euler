from euler_helpers import opt_sieve, bin_search

N = 1e6
primes = opt_sieve(int(N))
d_primes = {}
for p in primes:
    d_primes[p] = True
solved = False
for i in range(len(primes),0,-1)[::-1]:
    s = sum(primes[0:i])
    for j in range(0,len(primes)+1-i):
        if j == 0:
            s += primes[j+i-1]
        else:
            s -= primes[j-1]
            s += primes[j+i-1]
        if s > N:
            break
        if s in d_primes:
            print i,s
            #solved = True
    if solved:
        break

