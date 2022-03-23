# Power Set
array=[1,2,3]

set = [[]]

for a in array:

    for i in range(len(set)):

        set.append(set[i]+[a])

print(set)
