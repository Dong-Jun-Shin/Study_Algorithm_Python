# 2 x n 타일링
def solution(n):
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        # 추가된 가로가 1칸인 경우, 2칸인 경우 더하기
        dp.append((dp[i - 2] + dp[i - 1]) % (int(1e9) + 7))
    return dp[n]


print(solution(4))
print(solution(10))
print(solution(60000))
