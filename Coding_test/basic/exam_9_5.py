import sys
import heapq

# input 정의
input = sys.stdin.readline
# INF 정의
INF = int(1e9)

# 도시 갯수N, 통로 갯수M, 시작 도시C 받기
n, m, c = map(int, input().split())
# 통로 정보 시작 도시X, 도착 도시Y, 걸리는 시간Z 받기
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 최단 거리 리스트 정의
distance = [INF for _ in range(n + 1)]
# 메시지를 받은 도시 수
receiveCnt = 0
# 총 걸린 시간 정의
maxDistance = 0


# 다익스트라 알고리즘 구현
def dijkstra(start):
    # 우선순위 큐 정의
    q = []
    # 최단 거리 갱신
    distance[start] = 0
    # 우선순위 큐에 시작 노드 정보 삽입
    heapq.heappush(q, (0, start))
    while q:
        # 우선 순위 큐에 있는 노드 정보 pop
        dist, nodeIdx = heapq.heappop(q)
        # 큐에 담겨있던 거리값이 최단 거리 리스트의 nodeIdx 거리값보다 큰 경우 패스(이미 최단 거리가 아님)
        if distance[nodeIdx] < dist:
            continue
        # 시작 노드에 연결된 노드 확인
        for val in graph[nodeIdx]:
            cost = distance[nodeIdx] + val[1]
            # 연결된 노드와 값 최단 거리 리스트 업데이트
            distance[val[0]] = min(distance[val[0]], cost)
            # 우선순위 큐에 저장
            heapq.heappush(q, (cost, val[0]))


# 다익스트라 알고리즘 수행
dijkstra(c)


# 총 걸린 시간 반환
for d in distance:
    if d != INF:
        maxDistance = max(maxDistance, d)
        receiveCnt += 1

# INF가 아닌 값들의 개수, 제일 오래 걸리는 시간 출력 (시작 도시를 빼서 '-1' 필요)
print(receiveCnt - 1, maxDistance)
