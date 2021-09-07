# 커리큘럼
from collections import deque
import copy


def topology_sort():
    min_cost = copy.deepcopy(cost)
    q = deque()
    for i in range(1, n + 1):
        if indegrees[i] == 0:
            q.append(i)
    while q:
        node_idx = q.popleft()
        for node in graph[node_idx]:
            min_cost[node] = max(min_cost[node], min_cost[node_idx] + cost[node])
            indegrees[node] -= 1
            if indegrees[node] == 0:
                q.append(node)
    return min_cost


n = int(input())
indegrees = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
cost = [0] * (n + 1)

for i in range(1, n + 1):
    datas = list(map(int, input().split()))
    cost[i] = datas[0]
    for data in datas[1:-1]:
        indegrees[i] += 1
        graph[data].append(i)

print(topology_sort())

""" Test case
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
