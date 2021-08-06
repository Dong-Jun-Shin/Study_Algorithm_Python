# 플로이드(같은 노선에 대한 처리, 갈 수 없는 경우 0으로 처리)
n = int(input())
m = int(input())
INF = int(1e9)
dp = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, input().split())
    dp[start][end] = min(dp[start][end], cost)

for mid in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dp[i][j] == INF:
            print("0", end=' ')
        else:
            print(dp[i][j], end=' ')
    print()
