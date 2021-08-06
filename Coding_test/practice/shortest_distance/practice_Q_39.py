# 화성 탐사(전체 노드가 10000을 넘을 수 있으니 dijkstra 사용, graph를 cost표로 사용)
import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline


def dijkstra(graph, n):    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = []
    heapq.heappush(q, (0, 0, graph[0][0]))
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    while q:
        x, y, cost = heapq.heappop(q)
        if distance[x][y] < cost:
            continue
        for direction in directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            if not (0 <= next_x < n and 0 <= next_y < n):
                continue
            # 현재 x에 오기까지 필요한 cost와 다음에 필요한 비용의 합이 기존 판단한 비용보다 낮을 때 처리
            if distance[next_x][next_y] > cost + graph[next_x][next_y]:
                distance[next_x][next_y] = cost + graph[next_x][next_y]
                heapq.heappush(q, (next_x, next_y, distance[next_x][next_y]))
    
    return distance[n - 1][n - 1]
    

t = int(input())
result = []
for i in range(t):
    n = int(input())
    graph = []
    for j in range(n):
        graph.append(list(map(int, input().split())))
    result.append(dijkstra(graph, n))

for val in result:
    print(val)


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