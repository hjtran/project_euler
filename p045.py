from math import sqrt
import time

def isPentagonal(x):
    a = 3.0/2
    b = -1.0/2
    c = -x
    discr = b**2-4*a*c
    if discr < 0:
        return False
    else:
        x1 = (-b+sqrt(discr))/(2.0*a)
        x2 = (-b-sqrt(discr))/(2.0*a)

        return float.is_integer( max(x1,x2) )


x = 1
count = 0
for i in range(5,1000000,4):
    x += i
    if isPentagonal(x):
        print x
        count += 1
        if count == 2:
            break
