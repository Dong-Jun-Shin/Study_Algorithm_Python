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

bfs(graph, x, dist)
