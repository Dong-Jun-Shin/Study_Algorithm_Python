# 효율적인 화폐 구성
n, m = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

INF = int(1e9)
dp = [INF] * (m + 1)
dp[0] = 0
for n_val in n_list:
    for i in range(n_val, m + 1, n_val):
        dp[i] = min(dp[i], dp[i - n_val] + 1)

print(-1 if dp[m] == INF else dp[m])
