# 편집 거리
str_1 = input()
str_2 = input()

len_s1 = len(str_1)
len_s2 = len(str_2)
dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

for i in range(len_s1 + 1):
    dp[i][0] = i
for j in range(len_s2 + 1):
    dp[0][j] = j

for i in range(1, len_s1 + 1):
    for j in range(1, len_s2 + 1):
        if str_1[i - 1] == str_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

print(dp[len_s2][len_s1])
