# 특정 거리의 도시 찾기
from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline
n, m, k, x = map(int, input().rstrip().split())
min_dist = [INF] * (n + 1)
directions = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().rstrip().split())
    directions[a].append((b, 1))


def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        for next_node in directions[now]:
            if min_dist == INF:
                min_dist[next_node] = min_dist[now] + 1
                q.append(next_node)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    min_dist[start] = 0
    while q:
        dist, nodeIdx = heapq.heappop(q)
        if min_dist[nodeIdx] < dist:
            continue
        for i in directions[nodeIdx]:
            cost = dist + i[1]
            if cost < min_dist[i[0]]:
                min_dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(x)

str = ""
for i in range(1, n + 1):
    if min_dist[i] == k:
        str = str + f"{i}\n"

print(str if len(str) > 0 else "-1", end="")
