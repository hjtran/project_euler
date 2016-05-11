


palin_b10 = [n for n in range(1,int(1e6)) if str(n)==str(n)[::-1]]

palin_both = [n for n in palin_b10 if bin(n)[:1:-1]==bin(n)[2:] ]

print 'sum of palindromic numbers in b2 and b10 less than 1 mil is %d' % (sum(palin_both),)
