from time import time

start = time()
count89 = 0
for i in range(1,int(1e7)):
    while i != 1 and i != 89:
        s = 0
        for j in range(len(str(i))):
            s += (i%10)**2
            i /= 10
        i = s
    if i == 89:
        count89 += 1
print count89
print 'Elapsed time: %.5f seconds' % (time()-start,) 
