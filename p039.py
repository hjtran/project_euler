from math import sqrt

p_count = [0]*1010
for p in range(120,1001):
    print p
    for a in range(1,p):
        for b in range(a,p):
            c2 = a**2+b**2
            c = sqrt(c2)
            if a+b+c==p:
                p_count[p] += 1

print p_count.index(max(p_count))

