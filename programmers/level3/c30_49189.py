# 가장 먼 노드
from collections import deque


def solution(n, edges):
    graph = [[] for _ in range(n + 1)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    dist = [int(1e9)] * (n + 1)
    dist[1] = 0
    q = deque([(1, 0)])
    while q:
        s, cost = q.popleft()
        for e in graph[s]:
            if dist[e] > cost + 1:
                dist[e] = cost + 1
                q.append((e, cost + 1))

    dist = [val if val != int(1e9) else 0 for val in dist]
    return len([val for val in dist if val == max(dist)])
