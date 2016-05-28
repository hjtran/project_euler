
a_nums = []

for i in range(12,28123):
    divs = []
    for j in range(1,i/2+1):
        if i%j == 0:
            divs.append(j)
    if sum(divs) > i:
        a_nums.append(i)

sum_a_nums = [False]*28123

for i in range(len(a_nums)-1):
    for j in range(i,len(a_nums)):
        if a_nums[i]+a_nums[j] < 28123:
            sum_a_nums[a_nums[i]+a_nums[j]] = True

s = 0
for i,j in zip(sum_a_nums,range(len(sum_a_nums))):
    if not i:
        s += j

print s
