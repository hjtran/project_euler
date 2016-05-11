
d = '.'

i = 1
while len(d) < 1e6+1:
    d += str(i)
    i+=1

prod = reduce(lambda x,y:x*y, [ int(d[1*10**x]) for x in range(7) ],1)
print prod
