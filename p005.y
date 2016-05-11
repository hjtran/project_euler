from euler_helpers import sieve

primes_up_to_20 = sieve(20)
prod_factors = [0]*21 # each element represents number of that index as a factor

for i in range(1,21):
    i_factors = [0]*21
    d = i
    while d not in primes_up_to_20:
        for prime in primes_up_to_20[1:]:
            if d%prime==0:
                i_factors[prime] += 1
                d /= prime
                break
    i_factors[d] += 1

    prod_factors = [ max([prod_factors[j],i_factors[j]]) for j in range(len(i_factors))]

print prod_factors
prod = reduce(lambda x,y:x*y, [i**prod_factors[i] for i in range(len(prod_factors)) ],1)

print 'Smallest product easily divisble by numbers 1-20  is %d' % (prod,)

