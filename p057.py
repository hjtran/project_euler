count = 0
for iter in range(1000):
    num = 1
    den = 2
    for i in range(iter):
        num += den*2
        tmp = num
        num = den
        den = tmp
    num += den
    if len(str(num)) > len(str(den)):
        count += 1
print count
