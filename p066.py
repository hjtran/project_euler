from math import sqrt
x = 5


vals = []
m = (0,0)
for D in range(1,1001):
    if not float.is_integer(sqrt(D)):
        x = 2
        while not float.is_integer(sqrt((x**2.0-1)/D)):
            x += 1
        if x > m[1]:
            m = (D, x)
        print x

print m
