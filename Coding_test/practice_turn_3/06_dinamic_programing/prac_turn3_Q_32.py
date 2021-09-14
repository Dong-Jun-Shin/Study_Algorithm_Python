# 정수 삼각형
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dp = []
for i in range(n):
    dp.append([0] * len(array[i]))
dp[0][0] = array[0][0]

for i in range(1, n):
    for j in range(len(array[i])):
        for k in [-1, 0]:
            target_j = j + k
            if not (0 <= target_j < len(array[i - 1])):
                continue
            dp[i][j] = max(dp[i][j], array[i][j] + dp[i - 1][target_j])

print(max(dp[n - 1]))
