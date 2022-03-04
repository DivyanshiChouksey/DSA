# Majority Element
nums = [2,2,1,1,1,1,1,1,2,2]

# Naive Solution 
count = {}
for n in nums:
    if n in count:
        count[n]+=1
    else:
        count[n]=1
for key,value in count.items():
    if value>len(nums)/2:
        print(key)


# Optimized Solution
majority = nums[0]
count = 1
for num in nums[1:]:
    if num == majority:
        count+=1
    else:
        count-=1
        if count == 0:
            majority = num
            count = 1
print(majority)

