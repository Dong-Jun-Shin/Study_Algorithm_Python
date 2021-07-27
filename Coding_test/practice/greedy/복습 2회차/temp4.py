# 만들 수 없는 금액
n = int(input())
unitList = list(map(int, input().split()))

unitList.sort()
result = unitList[0]
for unit in unitList[1:]:
    if result < unit:
        break
    result += unit

print(result + 1)