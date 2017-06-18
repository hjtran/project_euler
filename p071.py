from math import ceil
from fractions import Fraction
d = 1000000

greatest = 0

for D in range(d,0,-1):
    D = D
    n = ceil((3.0/7)*D)
    while (n/D) >= 3.0/7:
        n -= 1
        #print('n reduced',n,D)
    if n/D > greatest:
        greatest = Fraction(n,D)
        #print(greatest)


print(greatest)
