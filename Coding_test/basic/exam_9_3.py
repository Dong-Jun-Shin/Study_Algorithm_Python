import sys

# input 정의
input = sys.stdin.readline
# INF 정의
INF = int(1e9)

# 노드 및 간선 개수 받기
v, e = map(int, input().split())

# 2차원 리스트를 INF로 초기화
graph = [[INF] * (v + 1) for _ in range(v + 1)]

# 자기 자신에 대해 0으로 초기화
for i in range(1, v + 1):
    graph[i][i] = 0

# 간선 정보를 받아서 자기 자신에 대한 값 초기화
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행(1부터 순차로 노드를 선택해서 확인)
for selNode in range(1, v + 1):
    for start in range(1, v + 1):
        for end in range(1, v + 1):
            graph[start][end] = min(graph[start][end], graph[start][selNode] + graph[selNode][end])

# 모든 노드에 대한 최단 거리 값 출력
for start in range(1, v + 1):
    for end in range(1, v + 1):
        if graph[start][end] == INF:
            print("INF", end='')
        else:
            print(f'{graph[start][end]:4}', end='')
    print()
