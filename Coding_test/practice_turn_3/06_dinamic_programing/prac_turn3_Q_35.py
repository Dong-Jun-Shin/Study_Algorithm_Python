# 못생긴 수
n = int(input())
dp = [0, 1]

i2, i3, i5 = 1, 1, 1
while True:
    i2_val, i3_val, i5_val = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
    val = min(i2_val, i3_val, i5_val)
    dp.append(val)
    if val % 2 == 0:
        i2 += 1
    if val % 3 == 0:
        i3 += 1
    if val % 5 == 0:
        i5 += 1

    if len(dp) > n:
        break

print(dp[n + 1])
