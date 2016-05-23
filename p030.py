
s = []
for i in range(2,2000000):
    digs = [ int(c) for c in str(i) ]
    if i == sum( [ dig ** 5 for dig in digs ] ):
        s.append(i)
print sum(s)
