from math import ceil, sqrt
from euler_helpers import bin_search
from euler_helpers import prime_factors as PFs

i = 10000
count = 0
while count!=4:
    if len(set(PFs(i)))==4:
        count += 1
    else:
        count = 0
    i += 1
print i-4
