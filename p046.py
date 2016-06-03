from euler_helpers import opt_sieve, bin_search

primes = opt_sieve(1e6)

n = 1000
squares = [2*(i**2) for i in range(1,n)]

solved = False
for i in range(3,int(1e6),2):
    if bin_search(primes,i)==-1:
        for sqr in squares:
            if bin_search(primes,i-sqr) != -1:
                break
        else:
            print i
            break
