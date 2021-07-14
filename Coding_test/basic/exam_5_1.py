# 인접 행렬 표현 방식
def makeAdjacencyMatrix():
    INF = 999999999     # 무한의 비용 선언

    # 2차원 리스트를 이용해 인접 행렬 표현
    graph = [
        [0, 7, 5],
        [7, 0, INF],
        [5, INF, 0]
    ]

    print(graph)


# 인접 리스트 표현 방식
def makeAdjacencyList():
    # 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
    graph = [[] for _ in range(3)]

    # 노드 0에 연결된 노드 정보 저장(노드, 거리)
    graph[0].append((1, 7))
    graph[0].append((2, 5))

    # 노드 1에 연결된 노드 정보 저장(노드, 거리)
    graph[1].append((0, 7))

    # 노드 2에 연결된 노드 정보 저장(노드, 거리)
    graph[2].append((0, 5))

    print(graph)


makeAdjacencyList()
makeAdjacencyMatrix()
