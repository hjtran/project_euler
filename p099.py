import math
with open('inputs/p099.txt','r') as infile:
    m = float('-inf')
    m_i = 0
    i = 1
    for line in infile.readlines():
        line = line.split(',')
        base = int(line[0])
        exp = int(line[1])
        
        if exp*math.log(base) > m:
            m = exp*math.log(base)
            m_i = i
        i+=1 
print m_i
