from euler_helpers import opt_sieve
from itertools import combinations as combs
from time import time
start = time()

def concat(a,b):
    return a*(10**len(str(b)))+b

def find_pps(s):
    # takes in a set of primes and returns
    # all a list of all possible prime pair sets
    # with one more prime including the primes in s
    
    list_s = list(s)
    intersection = set(pair_primes[s[0]])
    for p in s[1:]:
        intersection = intersection & pair_primes[p]
    return [(s+[x]) for x in intersection]


primes = opt_sieve(1e5)
prime_set = set(opt_sieve(1e8))

pair_primes = {}
for p in primes:
    pair_primes[p] = set()

pplist = []
for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        if (concat(primes[i],primes[j]) in prime_set and
                concat(primes[j],primes[i]) in prime_set):
            
            pair_primes[primes[i]].add(primes[j])
            pair_primes[primes[j]].add(primes[i])
            pplist.append( [primes[i],primes[j]] )

print 'pairs done processing'
print '%d pairs found' % (len(pplist),)
pp3list = set()
for pair in pplist:
    for x in find_pps(pair):
        pp3list.add(tuple(x))
pp4list = set()
for s in pp3list:
    for x in find_pps(list(s)):
        pp4list.add(tuple(x))
pp5list = set()
for s in pp4list:
    for x in find_pps(list(s)):
        pp5list.add(tuple(x))
print min(pp5list,key=lambda x:sum(x))
print 'Elapsed time: %.5f seconds' % (time()-start,) 
