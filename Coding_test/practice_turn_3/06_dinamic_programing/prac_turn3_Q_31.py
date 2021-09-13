# 금광
for _ in range(int(input())):
    n, m = map(int, input().split())
    array = []
    datas = list(map(int, input().split()))
    for i in range(0, n * m, m):
        array.append(datas[i:i + m])

    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = array[i][0]
    
    for j in range(1, m):
        for i in range(n):
            top, mid, bot = 0, 0, 0
            if 0 <= i - 1 < n:
                top = dp[i - 1][j - 1]
            if 0 <= i < n:
                mid = dp[i][j - 1]
            if 0 <= i + 1 < n:
                bot = dp[i + 1][j - 1]
            dp[i][j] = array[i][j] + max(top, mid, bot)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)


""" Test case
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
