
combs = [ set() for i in range(201) ]
denoms = [1, 2, 5, 10, 20, 50, 100, 200]
for d,idx in zip(denoms,range(len(denoms))):
    a = [0]*len(denoms)
    a[idx] += 1
    combs[d].add(tuple(a))

for i in range(2,201):
    for d,idx in zip(denoms,range(len(denoms))):
        if i > d:
            tmp = [list(x) for x in list(combs[i-d])]
            for t in tmp:
                t[idx] += 1
                combs[i].add(tuple(t))
        else:
            break
    print i

print len(combs[200])
