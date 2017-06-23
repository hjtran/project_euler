from math import sqrt,ceil
from euler_helpers import opt_sieve

n = 50000000
squares = []
cubes = []
fourths = []
for p in opt_sieve(ceil(sqrt(n))):
    squares.append(p**2)
    if p**3 < n:
        cubes.append(p**3)
        if p**4 < n:
            fourths.append(p**4)

expressible = set()
for s in squares:
    for c in cubes:
        for f in fourths:
            if s+c+f < n:
                expressible.add(s+c+f)

print(len(expressible))
    


