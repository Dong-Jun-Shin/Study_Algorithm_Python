# 음료수 얼려먹기
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input()))


def dfs(row, col):
    if 0 <= row and row < n and 0 <= col and col < m:
        if graph[row][col] == 0:
            graph[row][col] = 1
            dfs(row - 1, col)       # 북쪽
            dfs(row, col + 1)       # 동쪽
            dfs(row + 1, col)       # 남쪽
            dfs(row, col - 1)       # 서쪽
            return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
