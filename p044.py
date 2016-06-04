from euler_helpers import bin_search
from math import sqrt
import time
start = time.time()

N = 10000

a = 3
b = -1
b2 = b**2
poss = []
for i in range(1,N):
    #print i
    for j in range(i+1,N):
        (o1,o2) = (0.1,0.1)
        # calculate if there's a pentagonal sum
        c = -3*(j**2)+j-3*(i**2)+i
        discriminant = b2-4*a*c
        if discriminant > 0:
            x1 = (-b+sqrt(discriminant))/(2*a)
            x2 = (-b-sqrt(discriminant))/(2*a)
            o1 = max(x1,x2)
        
        if o1 > 0 and float.is_integer(o1):

            # calculate if there's a pentagonal diff
            c = -3*(j**2)+j+3*(i**2)-i
            discriminant = b2-4*a*c
            if discriminant > 0:
                x1 = (-b+sqrt(discriminant))/(2*a)
                x2 = (-b-sqrt(discriminant))/(2*a)
                o2 = max(x1,x2)

            if o2 > 0 and float.is_integer(o2):
                poss.append( (i,j,(j*(3*j-1))/2-(i*(3*i-1))/2 ) )
                print 'HIT(%d,%d)' % (i,j)
           
print 'Time elapsed: %.5f ' % (time.time()-start,) 
print poss 

