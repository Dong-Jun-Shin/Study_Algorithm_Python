import sys
import heapq

# input 정의
input = sys.stdin.readline
# INF 정의
INF = int(1e9)

# 노드 개수, 간선 개수 받기
v, e = map(int, input().split())
# 시작 노드 받기
start = int(input())

# 노드에 연결된 간선 정보를 담을 리스트 생성
graph = [[] for _ in range(v + 1)]
# 최단 거리 테이블 생성
distance = [INF] * (v + 1)
# 모든 간선 정보 받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 다익스트라 알고리즘 구현
def dijkstra(start):
    # 우선순위 큐 생성
    q = []
    # 시작 노드 설정
    distance[start] = 0
    # 우선순위 큐에 시작 노드 정보 삽입(거리, 노드 번호)
    heapq.heappush(q, (0, start))

    while q:
        # 노드를 꺼내서 연결된 노드 확인
        distVal, nodeIdx = heapq.heappop(q)
        # 현재 노드가 이미 처리되었으면 무시
        if distance[nodeIdx] < distVal:
            continue

        # 노드에 연결된 간선 확인
        for edge in graph[nodeIdx]:
            cost = distVal + edge[1]
            # 해당 경로를 이용해서 거리가 더 짧은지 판단
            if cost < distance[edge[0]]:
                distance[edge[0]] = cost
                # 해당 경로를 이용해서 연결된 다음 노드를 체크하도록 큐에 삽입
                heapq.heappush(q, (cost, edge[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)
# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, len(distance)):
    # 도달할 수 없는 경우 "INFINITY"라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])
