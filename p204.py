from time import time
from euler_helpers import opt_sieve
start = time()

# Problem Code

n = 100
#m = 15
m = 1000000000
primes = opt_sieve(n)
hams = [1]
ham_set = set(hams)

idx = 0
while idx < len(hams):
    for p in primes:
        if hams[idx]*p <= m and hams[idx]*p not in ham_set:
            ham_set.add(hams[idx]*p)
            hams.append(hams[idx]*p)
    idx += 1

#print(hams)
print(len(hams))



#

print('Time Elapsed: %.2fs' % (time()-start,))        
