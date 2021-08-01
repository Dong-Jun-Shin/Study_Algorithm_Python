# 경쟁적 전염
from collections import deque

INF = int(1e9)

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
location_virus = []
for i in range(n):
    data = list(map(int, input().split()))
    graph[i] = data
    for j in range(n):
        if data[j] != 0:
            location_virus.append((data[j], i, j))
location_virus.sort()
s, x, y = map(int, input().split())


def virus(_q, _type, _x, _y):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(4):
        next_x = _x + directions[i][0]
        next_y = _y + directions[i][1]
        if 0 > next_x or next_x >= n or 0 > next_y or next_y >= n:
            continue
        if graph[next_x][next_y] == 0:
            graph[next_x][next_y] = _type
            _q.append((_type, next_x, next_y))


# 초에 따른 사이클 구현
# bfs로 큐에 있는 작업 처리
q = deque(location_virus)
q.append((INF, 0, 0))
time_cnt = 0
while q:
    if time_cnt == s:
        break
    while True:
        v_type, start_x, start_y = q.popleft()
        if v_type == INF or time_cnt == s:
            break
        virus(q, v_type, start_x, start_y)
    q.append((INF, 0, 0))
    time_cnt += 1


# 특정 위치의 바이러스 타입 판단
if graph[x - 1][y - 1] == 0:
    result = 0
else:
    result = graph[x - 1][y - 1]

print(result)
