from collections import deque

# 노드와 간선 개수 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수 테이블 0 초기화
inDegree = [0] * (v + 1)
# 간선 정보를 받을 리스트 생성 및 받기
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1


# 위상 정렬 함수 정의
def topology_sort():
    # 결과 리스트 정의
    result = []
    # 큐 정의
    q = deque()

    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v + 1):
        if inDegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에 있는 원소 반환
        nodeIdx = q.popleft()
        # 결과 리스트에 삽입
        result.append(nodeIdx)
        # 해당 노드에 연결된 간선마다 정보 값 -1
        for edgeIdx in graph[nodeIdx]:
            inDegree[edgeIdx] -= 1
            # 해당 노드에 연결된 간선이 없으면 큐에 삽입
            if inDegree[edgeIdx] == 0:
                q.append(edgeIdx)

    # 결과 출력
    for i in result:
        print(i, end=' ')


# 위상 정렬 함수 수행
topology_sort()
