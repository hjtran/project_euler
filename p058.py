
gs = 1 # gridsize
diags = [1]
diff = 0
while gs < 501:
    gs += 1
    diff += 2
    diags.extend(range(diags[-1]+diff,diags[-1]+4*diff+1,diff))

print sum(diags)

