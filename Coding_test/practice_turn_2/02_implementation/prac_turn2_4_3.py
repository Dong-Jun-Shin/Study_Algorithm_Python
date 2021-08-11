# 게임 개발
import copy

n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = copy.deepcopy(graph)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited[x][y] = 1
result = 1
cnt = 0
while True:
    d = (d - 1) % 4
    nx = x + directions[d][0]
    ny = y + directions[d][1]
    if visited[nx][ny] == 0:
        x, y = nx, ny
        visited[nx][ny] = 1
        result += 1
        cnt = 0
        continue
    cnt += 1

    if cnt == 4:
        x -= directions[d][0]
        y -= directions[d][1]
        if graph[x][y] == 1:
            break
        cnt = 0

print(result)

""" Test case
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

5 5
1 1 0
1 1 1 1 1
1 0 0 0 1
1 0 1 0 1
1 0 1 0 1
1 1 1 1 1
"""
