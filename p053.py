from math import factorial as fact

def nCr(n,r):
    return fact(n) / (fact(r)*fact(n-r))

count = 0
for n in range(1,101):
    for r in range(n+1):
        if nCr(n,r) > 1e6:
            count += 1

print count
