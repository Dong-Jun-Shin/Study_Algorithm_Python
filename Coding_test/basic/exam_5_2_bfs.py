"""------------------------------book
from collections import deque


# BFS 함수 구현하기
def bfs(graph, start, visited):
    # 큐 초기화
    queue = deque([start])
    # 노드 방문 처리
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 인접 노드 탐색
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[v] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 8]
]

visited = [False] * len(graph)

bfs(graph, 1, visited)

----------------------------------"""

# ---------------------------------me
from collections import deque


# BFS 함수 구현하기
def bfs(graph, queue, visited):
    v = queue.popleft()
    if not visited[v]:
        # 노드 방문 처리
        visited[v] = True
        print(v, end=' ')
        # 인접 노드 탐색
        for i in graph[v]:
            queue.append(i)
            visited[v] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 8]
]

visited = [False] * len(graph)

queue = deque()
queue.append(1)
while True:
    bfs(graph, queue, visited)

    if not queue:
        break

# -----------------------------------
