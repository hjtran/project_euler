from euler_helpers import opt_sieve, polygon_range as prange
from time import time
start = time()
N = 1e8
primes = {}
for p in opt_sieve(N):
    primes[p] = True
print 'primes generated'
sl = 1 # sidelength
diags = [1]
diff = 0
num_primes = 0.0
while int(100*(num_primes / float(len(diags)))) > 9 or num_primes == 0:
    sl += 2
    diff += 2
    diags.extend(range(diags[-1]+diff,diags[-1]+4*diff+1,diff))
    num_primes = float(sum( [1 for x in diags if x in primes] ))
    if diags[-1] > N:
        raise Exception('Not enough primes generated')
    print num_primes/len(diags), diags[-1]
    #print diags[-1], prange(4,sl)[-1]
    

print sl
print 'time elapsed: %.5f seconds' % (time()-start,)
