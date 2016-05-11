
max = 0
for i in range(1000):
    for j in range(1000):
        prod = str(i*j)
        if prod == prod[::-1] and int(prod) > int(max):
            max = prod

print 'Largest palindromic product of 3 digit numbers is %s' % (max,)
