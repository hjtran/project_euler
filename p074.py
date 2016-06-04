from math import factorial as fact
from time import time 
start = time() 
def dig_fact(x):
    s = 0
    for i in range(len(str(x))):
        s += fact(x%10)
        x /= 10
    return s

t = [0]*3000000
t[1] = 1
t[2] = 1

count = 0
for i in range(1,1000000):
    term = i
    arr = []
    while term not in arr:
        arr.append(term)
        term = dig_fact(term)
    for x in arr:
        t[x] = len(arr)
    if t[term] == 60:
        count += 1
    if i == 60:
        print arr
print count,max(t)
print 'Elapsed time: %.5f seconds' % (time()-start,) 
