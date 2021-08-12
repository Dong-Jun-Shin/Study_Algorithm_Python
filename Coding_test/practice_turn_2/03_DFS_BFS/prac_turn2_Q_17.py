# 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
graph = []
lotation_virus = [[] for _ in range(k + 1)]
for i in range(n):
    datas = list(map(int, input().split()))
    graph.append(datas)
    for j in range(len(datas)):
        if datas[j] != 0:
            lotation_virus[datas[j]].append((i, j))

s, r_x, r_y = map(int, input().split())


def bfs():
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    time = 0
    q = deque()
    for i in range(1, len(lotation_virus)):
        for virus in lotation_virus[i]:
            x, y = virus
            q.append((x, y, i))
    q.append((-1, -1, -1))
    while q:
        if time == s:
            break
        
        x, y, k = q.popleft()

        if x == -1 and y == -1:
            time += 1
            if len(q) > 0:
                q.append((-1, -1, -1))
            continue

        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = k
                q.append((nx, ny, k))


bfs()
print(graph[r_x - 1][r_y - 1])
