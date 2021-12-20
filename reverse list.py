# reverse list
lst = [10,20,30,40,50,60,70]
for i in range(0,len(lst)//2):
    lst[i],lst[(len(lst)-1)-1] = lst[(len(lst)-1)-i],lst[i]
print(lst)
