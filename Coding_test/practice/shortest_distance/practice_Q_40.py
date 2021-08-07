# 숨바꼭질(다익스트라, 이진탐색, 함수로 정리)
import heapq
import bisect

n, m = map(int, input().split())
INF = int(1e9)
dp = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append((end, 1))
    graph[end].append((start, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    dp[start] = 0
    while q:
        start_idx, cost = heapq.heappop(q)
        if dp[start_idx] < cost:
            continue
        for end in graph[start_idx]:
            if dp[end[0]] > cost + end[1]:
                dp[end[0]] = cost + end[1]
                heapq.heappush(q, (end[0], end[1]))

dijkstra(1)

dist = 0
for val in dp:
    if val != INF:
        dist = max(dist, val)
num = bisect.bisect_left(dp, dist)
count = bisect.bisect_right(dp, dist) - bisect.bisect_left(dp, dist)

print(num, dist, count)
