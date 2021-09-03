# 숨바꼭질
import heapq
import bisect


def get_count_value(dist, value):
    right_idx = bisect.bisect_right(dist, value)
    left_idx = bisect.bisect_left(dist, value)
    return right_idx - left_idx


def dijkstra(start):
    q = []
    dist[0] = dist[start] = 0
    heapq.heappush(q, (start, 0))
    while q:
        start, cost = heapq.heappop(q)
        if dist[start] < cost:
            continue
        for end in graph[start]:
            if dist[end] > cost + 1:
                dist[end] = cost + 1
                heapq.heappush(q, (end, dist[end]))


n, m = map(int, input().split())
INF = int(1e9)
dist = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dijkstra(1)

sort_dist = sorted(dist)
for i in range(len(sort_dist) - 1, -1, -1):
    if sort_dist[i] != INF:
        break
    sort_dist[i] = 0

sel_dist = max(sort_dist)
sel_num = bisect.bisect_left(dist, sel_dist)
sel_cnt = get_count_value(sort_dist, sel_dist)

print(sel_num, sel_dist, sel_cnt)

""" Test Case
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""
