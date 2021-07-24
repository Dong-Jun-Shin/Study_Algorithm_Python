n, k = map(int, input().split())
unitList = []
for _ in range(n):
    unitList.append(int(input()))

result = 0
while k > 0:
    unit = unitList.pop()
    if unit <= k:
        result += (k // unit)
        k %= unit

# --------------------------------me
# 동전 0
# 동전 종류N, 가치의 합K
# n, k = map(int, input().split())
# unitList = []
# for _ in range(n):
#     unitList.append(int(input()))

# result = 0
# unitList.sort(reverse=True)
# for unit in unitList:
#     if unit <= k:
#         result += (k // unit)
#         k %= unit
#     if k <= 0:
#         break
# ----------------------------------

# 필요한 동전 개수의 최솟값
print(result)
