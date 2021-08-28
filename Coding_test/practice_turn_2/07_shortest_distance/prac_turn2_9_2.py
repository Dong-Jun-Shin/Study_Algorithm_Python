# 미래 도시
n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

dist = graph[1][k] + graph[k][x]
print(dist if dist < INF else -1)

""" Test case
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
(3)

4 2
1 3
2 4
3 4
(-1)
"""
