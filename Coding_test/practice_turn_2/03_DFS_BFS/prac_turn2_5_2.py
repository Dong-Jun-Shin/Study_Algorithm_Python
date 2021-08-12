# 음료수 얼려먹기
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]


def dfs(i, j):
    if 0 > i or i >= n or 0 > j or j >= m:
        return 0

    if graph[i][j] == 0 and visited[i][j] == False:
        visited[i][j] = True
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i + 1, j)
        dfs(i, j - 1)
        return 1
    return 0


count = 0
for i in range(n):
    for j in range(m):
        count += dfs(i, j)

print(count)

""" Test case
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
