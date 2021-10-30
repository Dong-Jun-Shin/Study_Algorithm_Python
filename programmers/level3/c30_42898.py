# 등굣길
# 주어지는 좌표가 열, 행이어서 puddles도 열, 행으로 구성
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0) or [j + 1, i + 1] in puddles:
                continue
            up = dp[i - 1][j] if 0 <= i - 1 < n else 0
            left = dp[i][j - 1] if 0 <= j - 1 < m else 0
            dp[i][j] = (up + left) % (int(1e9) + 7)
    return dp[n - 1][m - 1]

    
print(solution(5,4,[[2,1],[2,2],[2,3],[4,4],[4,3],[4,2]])) # 0
print(solution(4, 3, [[2, 2]])) # 4
print(solution(4, 3, [[1,3],[3,1]])) # 7
# print(solution(2, 2, [])) # 2
# print(solution(3, 3, [])) # 6
# print(solution(3, 3, [[2, 2]])) # 2
# print(solution(3, 3, [[2, 3]])) # 3
# print(solution(3, 3, [[1, 3]])) # 5
# print(solution(3, 3, [[1, 3], [3, 1]])) # 4
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3]])) # 2
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]])) # 1
# print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]])) # 0
# print(solution(4, 4, [[3, 2], [2, 4]])) # 7
# print(solution(100, 100, [])) # 690285631
