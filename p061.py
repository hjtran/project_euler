from euler_helpers import polygon_range as prange
from itertools import permutations as perms
from time import time
start = time()

class GetOutOfLoop( Exception ):
    pass

def isCyclic(a,b):
    if a % 100 == b / 100:
        return True
    else:
        return False

tri = [x for x in prange(3,200) if x < 10000 and x > 999]
rect = [x for x in prange(4,200) if x < 10000 and x > 999]
pent = [x for x in prange(5,200) if x < 10000 and x > 999]
hex = [x for x in prange(6,200) if x < 10000 and x > 999]
hept = [x for x in prange(7,200) if x < 10000 and x > 999]
oct = [x for x in prange(8,200) if x < 10000 and x > 999]

figurates = [tri, rect, pent, hex, hept, oct]

try:
    for p in perms(figurates):
        for n1 in p[0]:
            for n2 in p[1]:
                if isCyclic(n1,n2):
                    for n3 in p[2]:
                        if isCyclic(n2,n3):
                            for n4 in p[3]:
                                if isCyclic(n3,n4):
                                    for n5 in p[4]:
                                        if isCyclic(n4,n5):
                                            for n6 in p[5]:
                                                if isCyclic(n5,n6) and isCyclic(n6,n1):
                                                    print [n1,n2,n3,n4,n5,n6],n1+n2+n3+n4+n5+n6
                                                    raise GetOutOfLoop()
except GetOutOfLoop:
    pass

print 'Elapsed time: %.5f seconds' % (time()-start,)
