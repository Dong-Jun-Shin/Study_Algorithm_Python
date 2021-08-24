# 퇴사
n = int(input())
n_list = []
for _ in range(n):
    n_list.append(list(map(int, input().split())))

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    t, p = n_list[i]
    if 0 <= i + t <= n:
        dp[i] = p + max(dp[i + t:])

print(max(dp))
