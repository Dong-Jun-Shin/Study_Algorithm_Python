# 편집 거리(DP와 LCS 응용, 2차원 테이블 사용)
def ed(str1, str2):
    s1_len = len(str1)
    s2_len = len(str2)

    dp = [[0] * (s2_len + 1) for _ in range(s1_len + 1)]
    for i in range(s1_len + 1):
        dp[i][0] = i
    for j in range(s2_len + 1):
        dp[0][j] = j

    for i in range(1, s1_len + 1):
        for j in range(1, s2_len + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

    return dp


before_str = input()
after_str = input()

dp = ed(before_str, after_str)
print(dp[len(before_str)][len(after_str)])