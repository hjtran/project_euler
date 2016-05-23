import sys
from math import sqrt, ceil
from euler_helpers import sieve
def main(n):
    primes = sieve(int(ceil(sqrt(n))))
    prime_factors = set()

    d = n
    print len(primes)
    while d not in primes:
        for prime in primes:
            if d%prime==0:
                prime_factors.add(prime)
                d /= prime
    prime_factors.add(d)
    print 'Max prime factor of %d is %d' % (n,max(prime_factors))



if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Req int arg to calculate largest prime factor of'
        raise Exception()
    
    from time import time
    start = time()
    main(int(sys.argv[1]))
    print 'Script took %d seconds' % (time()-start,)

