# two num sum
# O(n^2) Time complexity
nums = [2,7,11,15]
target = 9
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)
