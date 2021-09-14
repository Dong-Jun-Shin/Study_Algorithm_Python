# 퇴사
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    next_job = i + array[i][0]
    if next_job <= n:
        dp[i] = array[i][1] + max(dp[next_job:])

print(max(dp))
