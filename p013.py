

with open('inputs/p013.txt','r') as infile:
    s = 0
    for line in infile.readlines():
        s += int(line.strip())

print str(s)[:10]
