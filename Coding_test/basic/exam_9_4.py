import sys
import heapq

# input 정의
input = sys.stdin.readline
# INF 정의
INF = int(1e9)

# v, e 받기
v, e = map(int, input().split())
# graph 간선 정보 받기
graph = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# k, x 받기(k:경유, x:도착)
k, x = map(int, input().split())

# graph 자기 자신 0으로 초기화
for i in range(1, v + 1):
    graph[i][i] = 0

# 플루이드 워셜 알고리즘 수행
for selNode in range(1, v + 1):
    for start in range(1, v + 1):
        for end in range(1, v + 1):
            graph[start][end] = min(graph[start][end], graph[start][selNode] + graph[selNode][end])

result = graph[1][k] + graph[k][x]

# 결과 출력
if result > INF:
    print("-1")
else:
    print(result)
