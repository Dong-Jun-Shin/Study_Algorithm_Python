# ATM
n = int(input())
pList = list(map(int, input().split()))

pList.sort()
result = 0
pSum = 0
for p in pList:
    result += p + pSum
    pSum += p

print(result)
