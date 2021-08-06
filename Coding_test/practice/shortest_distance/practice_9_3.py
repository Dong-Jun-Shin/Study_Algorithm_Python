# 전보
import heapq

INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, start = heapq.heappop(q)
        if distance[start] < dist:
            continue
        for end, end_dist in graph[start]:
            cost = dist + end_dist
            if distance[end] > cost:
                distance[end] = cost
                heapq.heappush(q, (cost, end))


dijkstra(c)

count = 0
max_dist = 0
for dist in distance:
    if dist != INF:
        count += 1
        max_dist = max(max_dist, dist)

print(count - 1, max_dist)
