# Bubble sort
# o(n^2) Time Complexity | o(1) Space complexity
lst = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
swapped = False
for i in range(0,len(lst)):
    for j in range(len(lst)-1-i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
            swapped = True
    if swapped == False:
        break
    else:
        swapped = False
print(lst)
