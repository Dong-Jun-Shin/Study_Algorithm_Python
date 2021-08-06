# 미래 도시
from collections import deque

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

x, k = map(int, input().split())

for via in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][via] + graph[via][j])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)
