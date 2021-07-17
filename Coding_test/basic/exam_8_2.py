""" ------------------------------------------book
# 식량창고 개수 받기
n = int(input())

# 창고별 식량의 개수 받기
nList = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = nList[0]
dp[1] = max(nList[0], nList[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])

print(dp[n - 1])
"""
# ----------------------------------------------me
# 식량창고 개수 받기
n = int(input())

# 창고별 식량의 개수 받기
nList = list(map(int, input().split()))


# DP 테이블 생성
def make_dp():
    dp = [0 for _ in range(n + 1)]
    for idx, val in enumerate(nList):
        dp[idx + 1] = val
    return dp


result = 0
for i in range(2, n):
    dp = make_dp()
    for j in range(3, n + 1):
        if j > i:
            dp[j] = max(dp[j], dp[j] + dp[j - i])
    result = max(max(dp), result)
print(result)
# -------------------------------------------------
