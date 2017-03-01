
# Fast powering algorithm
# Calcultes b^e % m
def fast_pow(b,e,m):

    if e == 1:
        return b % m
    elif e % 2 == 0:
        return fast_pow(b,e/2,m)**2%m
    else:
        return fast_pow(b,e/2,m)**2*b%m


print (28433*fast_pow(2,7830457,1e10)+1)%(1e10)
