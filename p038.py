from euler_helpers import opt_sieve

count = 0
for i in range(1,100000):
    pandigi = [0]*10
    j=0
    while sum(pandigi) < 9:
        j+=1
        for dig in str(j*i):
            pandigi[int(dig)] += 1
    if pandigi == [0]+[1]*9:
        count = [k*i for k in range(1,j+1)]
print count
