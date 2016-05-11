
sum = 0
for i in range(101):
    sum += i**2

sqr_of_sum = ((100*101)/2)**2
print 'difference between sum of the squares of the first 100 natural numbers and the square of the sum is %d' % (sqr_of_sum-sum,)
