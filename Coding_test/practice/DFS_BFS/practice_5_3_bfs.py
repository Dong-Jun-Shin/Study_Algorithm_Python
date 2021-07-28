# 음료수 얼려먹기
from collections import deque
import copy
    
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(input())


def bfs(visited, row, col):
    moveList = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque()
    q.append((row, col))
    while q:
        row, col = q.popleft()
        for move in moveList:
            nextRow = row + move[0]
            nextCol = col + move[1]
            if not(0 <= nextRow and nextRow < n and 0 <= nextCol and nextCol < m):
                continue
            if visited[nextRow][nextCol] == '0':
                q.append((nextRow, nextCol))
                visited[nextRow][nextCol] = '1'


visited = copy.deepcopy(graph)
result = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] != '1':
            result += 1
            visited[i][j] = '1'
            bfs(visited, i, j)

print(result)
