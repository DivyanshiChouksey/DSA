# Dutch national flag problem (0,1,2)
nums = [0,2,0,1,1,2,2]
low,mid,high = 0,0,len(nums)-1
while mid <= high:
    if nums[mid] == 0:
        nums[low],nums[mid] = nums[mid],nums[low]
        mid += 1
        low += 1
    elif nums[mid] == 2:
        nums[high],nums[mid] = nums[mid],nums[high]
        high -= 1
    else :
        mid += 1 
print(nums)

