
lycCount = 0
for i in range(10000):
    iters = 1
    n = i+int(str(i)[::-1])
    while iters < 50 and str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        iters += 1
    
    if str(n) != str(n)[::-1]:
        lycCount += 1

print lycCount
