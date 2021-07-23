from collections import deque
import copy

# 노드 개수 받기
v = int(input())
# 모든 노드에 대한 진입차수 0으로 초기화
inDegree = [0 for _ in range(v + 1)]
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0 for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 받아서 처리
for i in range(1, v + 1):
    # i번째 노드에 대한 시간과 출발 노드를 받기
    data = list(map(int, input().split()))
    time[i] = data[0]
    # 1부터 끝 원소 전까지 (1, n-1)
    for x in data[1:-1]:
        # 도착 노드에 간선을 카운트
        inDegree[i] += 1
        # 출발 노드에 도착 노드의 정보 삽입
        graph[x].append(i)


# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        nodeIdx = q.popleft()
        for i in graph[nodeIdx]:
            result[i] = max(result[i], result[nodeIdx] + time[i])
            inDegree[i] -= 1
            if inDegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])


topology_sort()
