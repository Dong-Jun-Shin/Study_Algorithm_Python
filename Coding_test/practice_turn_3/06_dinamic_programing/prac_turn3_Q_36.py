# 편집 거리
str_a = input()
str_b = input()

len_a = len(str_a)
len_b = len(str_b)

dp = [[0] * (len_a + 1) for _ in range(len_b + 1)]

for i in range(len_a + 1):
    dp[0][i] = i
for i in range(len_b + 1):
    dp[i][0] = i

for i in range(1, len_b + 1):
    for j in range(1, len_a + 1):
        if str_b[i - 1] == str_a[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

print(dp[len_b][len_a])

""" Test case
cat
cut

sunday
saturday
"""
