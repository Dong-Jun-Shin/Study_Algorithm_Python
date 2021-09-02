# 화성 탐사
import heapq

INF = int(1e9)
for _ in range(int(input())):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    dist = [[INF] * n for _ in range(n)]
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    dist[0][0] = graph[0][0]
    while q:
        cost, x, y = heapq.heappop(q)
        if dist[x][y] < cost:
            continue
        for direction in directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            if 0 > next_x or next_x >= n or 0 > next_y or next_y >= n:
                continue
            if dist[next_x][next_y] > cost + graph[next_x][next_y]:
                dist[next_x][next_y] = cost + graph[next_x][next_y]
                heapq.heappush(q, (dist[next_x][next_y], next_x, next_y))
        
    print(dist[n - 1][n - 1])

""" Test Case
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""
