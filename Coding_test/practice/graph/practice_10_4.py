# 커리큘럼(위상정렬, 선수과목, 최대시간 처리)
from collections import deque
import copy

n = int(input())

graph = [[] for _ in range(n + 1)]
cost = [0] * (n + 1)
indegree = [0] * (n + 1)
for i in range(1, n + 1):
    datas = list(map(int, (input().split())))
    cost[i] = datas[0]
    for data in datas[1:-1]:
        graph[data].append(i)
        indegree[i] += 1


def topology_sort():
    result = copy.deepcopy(cost)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        selNodeIdx = q.popleft()
        for i in graph[selNodeIdx]:
            result[i] = max(result[i], result[selNodeIdx] + cost[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


topology_sort()
