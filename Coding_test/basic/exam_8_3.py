# 1 * 2 / 2 * 1 / 2 * 2 의 경우

# n이 한 칸씩 늘어날 때마다, 가능한 경우의 수는 1개의 경우당 '이전 경우의 수 * 1'이기 때문에
# 1칸 여유있을 시, 1 * 2로 구성된 1가지 경우
# 2칸 여유있을 시, 2 * 1로 구성된 1가지 경우
# 2칸 여유있을 시, 2 * 2로 구성된 1가지 경우
# 가 나올 수 있게 된다. 그래서 i번째 경우의 수는 각각 이전 경우의 수를 더한 값이 된다. 
# dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 2]

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
