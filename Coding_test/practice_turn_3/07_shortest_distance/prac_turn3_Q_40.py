# 숨바꼭질
from collections import deque
import bisect

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s_idx, e_idx = map(int, input().split())
    graph[s_idx].append(e_idx)
    graph[e_idx].append(s_idx)

INF = int(1e9)
dist = [INF] * (n + 1)
dist[1] = 0
q = deque()
q.append((1, 0))
while q:
    s_idx, cost = q.popleft()
    if dist[s_idx] < cost:
        continue
    for e_idx in graph[s_idx]:
        if dist[e_idx] > cost:
            dist[e_idx] = cost + 1
            q.append((e_idx, cost + 1))

dist = sorted(dist)
for i in range(len(dist) - 1, -1, -1):
    if dist[i] != INF:
        break
    dist[i] = 0

p_dist = max(dist)
p_num = bisect.bisect_left(dist, p_dist)
p_cnt = bisect.bisect_right(dist, p_dist) - p_num

print(p_num, p_dist, p_cnt)

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
