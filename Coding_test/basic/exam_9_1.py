import sys

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
# 방문 체크 리스트 생성
visited = [False] * (v + 1)
# 최단 거리 테이블 생성
distance = [INF] * (v + 1)
# 모든 간선 정보 받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중, 가장 최단 거리의 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    # 현재 확인하는 노드까지의 거리가 가장 짧으면서 아직 방문하지 않은 노드 찾기
    for i in range(1, len(distance)):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


# 다익스트라 알고리즘 구현
def dijkstra(start):
    # 시작 노드 거리와 방문 체크
    distance[start] = 0
    visited[start] = True
    # 시작 노드와 연결된 노드 확인 후 업데이트
    for val in graph[start]:
        distance[val[0]] = val[1]

    # 시작 노드를 제외한 노드에 대해 반복((graph=v+1) - 1)
    for _ in range(1, len(graph) - 1):
        # 다음 최단 거리 노드를 가져오기
        index = get_smallest_node()
        # 해당 노드에 대한 방문처리
        visited[index] = True
        # 연결된 노드 확인
        for val in graph[index]:
            # 가져온 노드 정보를 이용해서 최솟값을 업데이트
            distance[val[0]] = min(distance[val[0]], distance[index] + val[1])


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
