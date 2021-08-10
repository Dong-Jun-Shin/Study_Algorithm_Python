# 최종 순위(위상정렬, 2차원 그래프 표현)
# 높은 순위가 낮은 순위로 향하도록(=진입차수), 일관성이 있는지 판단(=사이클 발생 여부), 순위를 알 수 없는 경우(=큐에 2개 이상 들어오는 경우)
import sys
from collections import deque


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
        nodeIdx = q.popleft()
        result.append(nodeIdx)
        for j in range(1, n + 1):
            if graph[nodeIdx][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    
    if cycle:
        return "IMPOSSIBLE"
    elif not certain:
        return "?"
    else:
        string = ""
        for char in result:
            string += f"{char} "
        return string


input = sys.stdin.readline

result = []
test = int(input())
for _ in range(test):
    n = int(input())
    prev_rank = list(map(int, input().split()))
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n):
            graph[prev_rank[i]][prev_rank[j]] = True
            indegree[prev_rank[j]] += 1

    m = int(input())
    for _ in range(m):
        now, prev = map(int, input().split())
        if graph[now][prev]:
            graph[now][prev] = False
            graph[prev][now] = True
            indegree[prev] -= 1
            indegree[now] += 1
        else:
            graph[now][prev] = True
            graph[prev][now] = False
            indegree[prev] += 1
            indegree[now] -= 1
            
    result.append(topology_sort(n, graph, indegree))

for char in result:
    print(char)
