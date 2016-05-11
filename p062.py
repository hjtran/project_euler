

cube_hash = {'0':[0,[]]}

i = 2
digits = 1
while 5 not in [str_cube[0] for str_cube in cube_hash.values()]:
    
    while (i**3)/(10**digits) == 0:
        sorted_str_of_cube = ''.join(sorted(str(i**3)))
        if sorted_str_of_cube not in cube_hash:
            cube_hash[sorted_str_of_cube] = [1,[i**3]]
        else:
            cube_hash[sorted_str_of_cube][0] += 1
            cube_hash[sorted_str_of_cube][1].append(i**3)

        i += 1

    digits += 1
    print str(i)

for item in cube_hash.items():
    if item[1][0] == 5:
        smallest_cube = min(item[1][1])


print 'the smallest cube for which exactly five permutations of its digits are cube is %d' % (smallest_cube,)



