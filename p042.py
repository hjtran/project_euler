from euler_helpers import bin_search
tri = []
num = 0

for i in range(500):
    num += i
    tri.append(num)


with open('inputs/p042.txt','r') as infile:
    count = 0
    words = infile.readline().strip().split(',')
    words = [w.strip('"') for w in words]
    for word in words:
        word_num = sum([ord(c)-ord('A')+1 for c in word])
        if bin_search(tri,word_num) != -1:
            count += 1
print count
