# 미로 탈출
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input()))


def bfs(start, end):
    moveList = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque()
    q.append((start, end))
    while q:
        row, col = q.popleft()
        for move in moveList:
            nextRow = row + move[0] 
            nextCol = col + move[1]
            if 0 <= nextRow and nextRow < n and 0 <= nextCol and nextCol < m:
                if graph[nextRow][nextCol] == 1:
                    graph[nextRow][nextCol] = graph[row][col] + 1
                    q.append((nextRow, nextCol))


bfs(0, 0)

print(graph[n - 1][m - 1])
