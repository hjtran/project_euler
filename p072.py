from fractions import Fraction

rpf = set() #reduced proper fractions
for D in range(2,101):
    for d in range(2,D+1):
        for n in range(1,d):
            rpf.add(Fraction(n,d))

    print len(rpf),D

