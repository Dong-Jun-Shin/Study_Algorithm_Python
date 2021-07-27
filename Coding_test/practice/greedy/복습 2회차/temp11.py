# 주유소
n = int(input())
distList = list(map(int, input().split()))
costList = list(map(int, input().split()))

minCost = costList[0]
totDist = distList[0]
result = 0
for i in range(1, len(costList) - 1):
    if minCost > costList[i]:
        result += totDist * minCost
        minCost = costList[i]
        totDist = 0
    totDist += distList[i]
else:
    result += totDist * minCost

print(result)
