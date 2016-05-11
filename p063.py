
nums = range(1,10)

count = 0
power = 1
while len(nums)>0:
    nums = [num for num in nums if len(str(num**power))==power]
    count += len(nums)

    print str(nums) + 'to the %d have %d digits' %(power,power)
    power += 1
 
print 'There are %d many n-digit positive integers exist which are also an nth power' % (count,)
