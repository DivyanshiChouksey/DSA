# Majority Element 2
nums = [1,1,1,2,2,3,3,3]

# Naive Solution 
count = {}
ans = []
for n in nums:
    if n in count:
        count[n]+=1
    else:
        count[n]=1
for key,value in count.items():
    if value>len(nums)/3:
        ans.append(key)
print(ans)


# Optimized Solution
n = len(nums)/3
num1 = num2 = float('inf')
c1 = c2 = 0

for num in nums:

    if num1==num:
        c1+=1
    elif num2 == num:
        c2+=1
    elif c1 ==0:
        num1 = num
        c1=1
    elif c2 == 0:
        num2 = num
        c2=1
    else:
        c1-=1
        c2-=1
res = []
for x in [num1, num2]:
    if nums.count(x) > len(nums) // 3:
        res.append(x)
print( res) 
