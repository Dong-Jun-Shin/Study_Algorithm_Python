# 전보
from collections import deque

n, m, c = map(int, input().split())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

q = deque()
q.append(c)
visited[c] = True
max_cost = 0
nation_cnt = 0
while q:
    start = q.popleft()
    for end, cost in graph[start]:
        if visited[end] is False:
            visited[end] = True
            max_cost = max(max_cost, cost)
            nation_cnt += 1
            q.append(end)

print(nation_cnt, max_cost)

""" Test case
3 2 1
1 2 4
1 3 2
"""
