# 화성 탐사
from collections import deque

INF = int(1e9)
result = ""
for _ in range(int(input())):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    dp = [[INF] * n for _ in range(n)]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dp[0][0] = graph[0][0]
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for direction in directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            if not (0 <= next_x < n and 0 <= next_y < n):
                continue
            if dp[next_x][next_y] > dp[x][y] + graph[next_x][next_y]:
                dp[next_x][next_y] = dp[x][y] + graph[next_x][next_y]
                q.append((next_x, next_y))
    
    result += f"{dp[n - 1][n - 1]}\n"

print(result)

""" Test Case
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""
