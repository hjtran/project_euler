
d = set()
for a in range(10000):
    divisors = []
    for j in range(1,a):
        if a%j==0:
            divisors.append(j)
    
    b = sum(divisors)
    divisors = []
    for j in range(1,b):
        if b%j==0:
            divisors.append(j)
    db = sum(divisors)

    if a != b and db == a:
        if a < 10000:
            d.add(a)
        if db < 10000:
            d.add(b)

print sum(list(d))
