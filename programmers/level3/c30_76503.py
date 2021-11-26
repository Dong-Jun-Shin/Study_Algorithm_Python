# 모두 0으로 만들기
# 양방향 그래프에 대한 위상 정렬
from collections import deque

def solution(a, edges):
    if sum(a) != 0:
        return -1

    answer = 0
    n = len(a)
    indegrees = [0] * n
    graph = [[] for _ in range(n)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
        indegrees[s] += 1
        indegrees[e] += 1

    visited = [False for _ in range(n)]
    q = deque()
    for i in range(n):
        if indegrees[i] - 1 == 0:
            q.append(i)

    while q:
        start = q.popleft()
        if a[start] == 0: continue
        for end in graph[start]:
            if visited[end]: continue 
            answer += abs(a[start])
            a[end] += a[start]
            a[start] = 0
            visited[start] = True
            indegrees[end] -= 1
            if indegrees[end] - 1 == 0:
                q.append(end)
    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
print(solution([0, 1, 0], [[0, 1], [1, 2]]))
