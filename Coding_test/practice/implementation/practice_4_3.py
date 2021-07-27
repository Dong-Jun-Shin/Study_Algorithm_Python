from collections import deque
import copy

# 게임 개발
n, m = map(int, input().split())
curX, curY, curWay = map(int, input().split())

way = [(-1, 0), (0, 1), (1, 0), (0, -1)]
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

visited = copy.deepcopy(graph)

q = deque()
q.append((curX, curY, curWay))
result = 1
visited[curX][curY] = 1
cnt = 0
while q:
    x, y, i = q.popleft()
    #(북0, 동1, 남2, 서3)
    nextX = x + way[i][0]
    nextY = y + way[i][1]
    if not (0 <= nextX and nextX < n) and (0 <= nextY and nextY < m):
        continue
    if graph[nextX][nextY] == 0 and visited[nextX][nextY] == 0:
        result += 1
        visited[nextX][nextY] = 1
        cnt = 0
        q.append((nextX, nextY, i))
    elif cnt < 4:
        cnt += 1
        q.append((x, y, (i + 1) % 4))

print(result)
