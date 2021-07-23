# 만들 수 없는 금액
n = int(input())
unitList = list(map(int, input().split()))

unitList.sort(reverse=True)
for i in range(1, 1000000):
    num = i
    for unit in unitList:
        if num >= unit:
            num -= unit
    if not (num == 0):
        break

print(i)
