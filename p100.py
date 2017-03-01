from math import sqrt

def quadratic_solver(a,b,c):
    discriminant = b**2-4*a*c


    return ( (-b+sqrt(discriminant))/(2.0*a), (-b-sqrt(discriminant))/(2.0*a) )


for n in range(int(10**11-100),int(10**11+100000)):
    soln_found = False
    soln = None

    roots = quadratic_solver(2,-2,-(n**2-n))

    for r in roots:
        if r > 0 and (r*(r-1))/(n*(n-1)) > 0.499999 and (r*(r-1))/(n*(n-1)) < 0.500001 and r % 1 < 0.0000001:
            soln = (int(r),n)
            soln_found = True

    if soln_found:
        break


print soln

blue = soln[0]
total = soln[1]

print (blue*(blue-1))/float(total*total-1)


