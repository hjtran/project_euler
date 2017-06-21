from math import ceil,sqrt

K = 12000
# minPS[k] is minPS for k=k
minPS = [float('Inf') for _ in range(K+1)]

#T = [ [],
        #[],
        #[],
        #[],
        #[2]
    #]

T = [ [1] for _ in range(K*3) ]

for k in range(4,K*3):
    for fac in range(2,ceil(sqrt(k))+1):
        if k == int(k/fac)*fac:
            diff = k-(int(k/fac)+fac)
            for p in T[fac]:
                for q in T[int(k/fac)]:
                    T[k].append(p+q+diff)
                    if (p+q+diff) >= len(minPS):
                        continue
                    minPS[p+q+diff] = min(minPS[p+q+diff],k)

print(sum(set([ps for ps in minPS if ps!=float('Inf')])))

