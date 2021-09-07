# 최종 순위
from collections import deque
import sys


def topology_sort(n, graph, indegree):
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    result = []
    for _ in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        node_idx = q.popleft()
        result.append(node_idx)
        for i in range(1, n + 1):
            if graph[node_idx][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if cycle:
        return "IMPOSSIBLE"
    elif not certain:
        return "?"
    else:
        string = ""
        for val in result:
            string += f"{val} "
        return string


input = sys.stdin.readline
result = []
for _ in range(int(input())):
    n = int(input())
    n_list = list(map(int, input().split()))
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n):
            graph[n_list[i]][n_list[j]] = True
            indegree[n_list[j]] += 1

    m = int(input())
    for _ in range(m):
        high, low = list(map(int, input().split()))
        if graph[high][low]:
            graph[high][low] = False
            graph[low][high] = True
            indegree[high] += 1
            indegree[low] -= 1
        else:
            graph[high][low] = True
            graph[low][high] = False
            indegree[high] -= 1
            indegree[low] += 1

    result.append(topology_sort(n, graph, indegree))

for val in result:
    print(val)
