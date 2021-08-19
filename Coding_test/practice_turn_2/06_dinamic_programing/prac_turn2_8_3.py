# 개미 전사
n = int(input())
n_list = list(map(int, input().split()))

dp = [0] * 100

dp[0] = n_list[0]
dp[1] = max(n_list[0], n_list[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + n_list[i])

print(dp[n - 1])
