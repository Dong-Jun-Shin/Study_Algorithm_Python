""" ------------------------------------------book
# 화폐 종류 n, 가치의 합 m 받기
n, m = map(int, input().split())

# 주어지는 각 화폐 가치 받기
nList = []
for i in range(n):
    nList.append(int(input()))

# DP 테이블 생성 (화폐 구성이 될 수 없는 수를 초기값으로 설정)
dp = [10001 for _ in range(m + 1)]
dp[0] = 0

for val in nList:
    for i in range(val, m + 1):
        dp[i] = min(dp[i], dp[i - val] + 1)

if dp[m] > 10000:
    dp[m] = -1

print(dp[m])
"""
# ----------------------------------------------me
# 화폐 종류 n, 가치의 합 m 받기
n, m = map(int, input().split())

# 주어지는 각 화폐 가치 받기
nList = []
for i in range(n):
    nList.append(int(input()))

nList.sort(reverse=True)
result = 0
for val in nList:
    result += m // val
    m %= val
    if m < nList[n - 1] and m != 0:
        result = -1
        break

print(result)
# -------------------------------------------------
