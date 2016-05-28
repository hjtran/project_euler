prods = set()
for a in range(1,2000):
    for b in range(1,2000):
        c = a*b
        pandig = [0]*10
        for dig in str(a)+str(b)+str(c):
            pandig[int(dig)] += 1
        if pandig[:] == [0]+[1]*9:
            print a,b,c
            prods.add(c)

print prods
print sum(prods)
