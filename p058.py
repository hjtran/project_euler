from euler_helpers import opt_sieve, polygon_range as prange
from math import sqrt
from time import time

def isPrime(x):
    if x <= primes[-1]:
        return x in prime_set
    elif x % 2 == 0:
        return False
    else:
        for p in primes:
            if p > sqrt(x):
                break
            elif x%p == 0:
                return False

        return True


start = time()
N = 1e7

primes = opt_sieve(N)
prime_set = set(primes)

print 'primes generated'
sl = 1 # sidelength
diags = [1]
diff = 0
num_primes = 0.0
while int(100*(num_primes / float(len(diags)))) > 9 or num_primes == 0:
    sl += 2
    diff += 2
    diags.extend(range(diags[-1]+diff,diags[-1]+4*diff+1,diff))
    num_primes += float(sum( [1 for x in diags[-4:-1] if isPrime(x)] ))
    print num_primes/len(diags), diags[-1]
    

print sl
print 'time elapsed: %.5f seconds' % (time()-start,)
