from euler_helpers import opt_sieve

d = 1000
primes = opt_sieve(d)
primes.remove(2)
primes.remove(5)

longest = 0
maxcount = 0

for p in primes:
    digs = []
    x = 1
    for i in range(10000):
        x *= 10
        digs.append(x/p)
        x %= p
    digs = digs[1:]
    cycle = 1
    while digs[0:0+cycle] != digs[cycle+0:cycle+cycle]:
        cycle += 1
        if cycle > 10000:
            cycle = 1
            break
    if cycle > maxcount and cycle != p-1:
        maxcount = cycle
        longest = p
    print p,cycle,digs[:10]
print longest
