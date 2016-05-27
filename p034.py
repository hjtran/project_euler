from math import factorial

count = 0
for i in range(3,1000001):
    if i == sum([ factorial(int(d)) for d in str(i) ] ):
        count += i
        print i
print count
