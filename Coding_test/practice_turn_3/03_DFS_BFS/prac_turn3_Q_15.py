# 특정 거리의 도시 찾기
from collections import deque


def bfs(graph, start, dist):
    q = deque()
    q.append((start, 0))
    dist[start] = 0
    while q:
        start, cost = q.popleft()
        for e, c in graph[start]:
            if dist[e] > cost + c:
                dist[e] = cost + c
                q.append((e, dist[e]))


INF = int(1e9)
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

dist = [INF] * (n + 1)
bfs(graph, x, dist)

for i in range(n + 1):
    if dist[i] == k:
        print(i)

if k not in dist:
    print(-1)
