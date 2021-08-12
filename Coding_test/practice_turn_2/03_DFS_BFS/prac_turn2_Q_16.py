# 연구소
from collections import deque
import copy

n, m = map(int, input().split())
graph = []
virus = []
for i in range(n):
    datas = list(map(int, input().split()))
    graph.append(datas)
    for j in range(m):
        if datas[j] == 2:
            virus.append((i, j))

max_safe_zone = 0


def virus_simulation():
    global graph, virus
    new_graph = copy.deepcopy(graph)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for v_x, v_y in virus:
        q = deque()
        q.append((v_x, v_y))
        while q:
            x, y = q.popleft()
            for direction in directions:
                nx = x + direction[0]
                ny = y + direction[1]
                if 0 > nx or nx >= n or 0 > ny or ny >= m:
                    continue
                if new_graph[nx][ny] == 0:
                    new_graph[nx][ny] = 2
                    q.append((nx, ny))
    return new_graph


def dfs(wall):
    global max_safe_zone
    if wall < 3:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    wall += 1
                    dfs(wall)
                    wall -= 1
                    graph[i][j] = 0
    else:
        new_graph = virus_simulation()
        safe_zone = 0
        for i in range(n):
            for j in range(m):
                if new_graph[i][j] == 0:
                    safe_zone += 1
        max_safe_zone = max(max_safe_zone, safe_zone)


dfs(0)
print(max_safe_zone)
