# 1 * 2 / 2 * 1 / 2 * 2 의 경우

# n = 0   0
# n = 1   1
# n = 2   3
# n = 3   5
# n = 4

# 가로 n 받기
n = int(input())

# DP 테이블 생성
dp = [0 for _ in range(n + 1)]
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    # dp[i] = dp[i - 1](1x2) + dp[i - 2](2x1) + dp[i - 2](2x2)
    # 796,796을 나눠서 결과값이 굉장히 커지는 것을 방지
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

print(dp[n])
