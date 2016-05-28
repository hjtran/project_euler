
with open('inputs/p022.txt','r') as infile:
    names = [x.strip('"') for x in infile.readline().split(',')]
    names.sort()
    s = 0
    pos = 1
    for name in names:
        score = sum([ord(c)-64 for c in name])
        s += score*pos
        pos += 1

print s
