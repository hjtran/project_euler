from itertools import permutations

p = list(permutations('0123456789'))
p.sort()
print p[999999]
