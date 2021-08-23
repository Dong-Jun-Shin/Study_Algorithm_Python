# 정수 삼각형
import copy

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(list(map(int, input().split())))

dp = copy.deepcopy(n_list)

for i in range(n - 1):
    for j in range(len(n_list[i])):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + n_list[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + n_list[i + 1][j + 1])

print(max(dp[n - 1]))
