# 못생긴 수
n = int(input())

dp = [0] * n
dp[0] = 1

i2, i3, i5 = 0, 0, 0
next_2, next_3, next_5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(next_2, next_3, next_5)
    if dp[i] == next_2:
        i2 += 1
        next_2 = dp[i2] * 2
    if dp[i] == next_3:
        i3 += 1
        next_3 = dp[i3] * 3
    if dp[i] == next_5:
        i5 += 1
        next_5 = dp[i5] * 5

print(dp[n - 1])
