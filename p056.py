m = 0
for a in range(1,100):
    for b in range(1,100):
        m = max(m,sum( [int(d) for d in str(a**b)] ) )
print m
