# maximum wealth
accounts = [[2,3],[2,1]]
maxWealth = 0
for account in accounts :
    wealth = sum(account)
    maxWealth = max(maxWealth,wealth)
print(maxWealth)
