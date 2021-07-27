# 동전 0
n, k = map(int, input().split())

unitList = [0] * n 
for i in range(n):
    unitList[i] = int(input())

unitList.sort(reverse=True)

result = 0
for unit in unitList:
    if k < unit:
        continue
    result += k // unit
    k %= unit
    if k <= 0:
        break

print(result)
