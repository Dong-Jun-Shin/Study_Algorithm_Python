# 금광
result = []
for _ in range(int(input())):
    n, m = map(int, input().split())

    array = [[] for _ in range(n)]
    data = list(map(int, input().split()))
    for i in range(0, n * m, m):
        array[i].append(data[i:i + m])

    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = array[i][0]

    for j in range(1, m):
        for i in range(n):
            for direction in [-1, 0, 1]:
                next_i = i + direction
                if next_i < 0 or next_i >= n:
                    continue
                dp[i][j] = max(dp[i][j], dp[next_i][j - 1] + array[i][j])

    max_val = 0
    for i in range(n):
        max_val = max(max_val, dp[i][m - 1])
    result.append(max_val)

print(result)

""" Test case
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
