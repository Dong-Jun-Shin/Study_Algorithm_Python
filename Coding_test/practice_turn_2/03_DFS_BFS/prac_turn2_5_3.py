# 미로 탈출
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(start_x, start_y):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visitied = [[False] * m for _ in range(n)]
    q = deque()
    visitied[start_x][start_y] = True
    q.append((start_x, start_y))
    while q:
        x, y = q.popleft()
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if graph[nx][ny] != 0 and not visitied[nx][ny]:
                graph[nx][ny] += graph[x][y]
                visitied[nx][ny] = True
                q.append((nx, ny))


bfs(0, 0)
print(graph[n - 1][m - 1])