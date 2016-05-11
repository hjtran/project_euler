
fib_seq = [1,2]
even_fib_sum = 2

while fib_seq[-1]+fib_seq[-2] < 4e6:
    fib_seq.append(fib_seq[-1]+fib_seq[-2])
    if fib_seq[-1]%2==0:
        even_fib_sum += fib_seq[-1]

print 'Sum of even elements of fib elements below 4e7 equals %d' % (even_fib_sum,)
