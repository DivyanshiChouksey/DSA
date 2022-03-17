# Can Place Flowers
flowerbed = [1,0,0,0,1]
n = 1
if n==0:
    print (True)
st=[0]+flowerbed+[0]
i = 1
while i<len(st)-1:
    if st[i-1]==0 and st[i]==0 and st[i+1]==0:
        n-=1
        i+=1
        if n==0:
            print(True)
    i+=1
print(n==0)
