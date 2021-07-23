# 만들 수 없는 금액
n = int(input())
unitList = list(map(int, input().split()))

"""-------------------------book
# 작은 단위부터 더해서, 해당 값까지의 수는 만들어진다.
# 하지만 다음 단위가 더 클 경우, 현재 target값은 만들 수 없게 된다.
# (target=12, +unit:13 -> 12를 만들 수 없다)
unitList.sort()
target = 1
for unit in unitList:
    if target < unit:
        break
    target += unit
"""
# ----------------------------me
# 큰 단위부터 현재 i에서 뺀다.
# 단위를 다 돌렸을 때, 0이 되면 만들 수 있는 수이다.
# 0이 나오지 않을 때까지 계산한다.
unitList.sort(reverse=True)
for i in range(1, 1000000):
    num = i
    for unit in unitList:
        if num >= unit:
            num -= unit
    if not (num == 0):
        break
# ------------------------------

print(i)
