# 정확한 순위(플로이드 워셜, 서로 도달할 수 있는지 여부 판단)
from collections import deque

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1

for mid in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
             graph[i][j] = min(graph[i][j], graph[i][mid] + graph[mid][j])

result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if INF != graph[i][j] or INF != graph[j][i]:
            count += 1
    if count == n:
        result += 1

print(result)

# -------------------------------------------------------------- me
# from collections import deque

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for i in range(m):
#     start, end = map(int, input().split())
#     graph[start].append(end)

# def check_node(nodeIdx):
#     visited = [False] * (n + 1)
#     visited[0] = visited[nodeIdx] = True
#     for j in range(1, m):
#             q = deque()
#             q.append(j)
#             while q:
#                 start = q.popleft()
#                 for end in graph[start]:
#                     if end == nodeIdx:
#                         visited[j] = True
#                         break
#                     elif j == nodeIdx:
#                         visited[end] = True
#                     q.append(end)
#     if False in visited:
#         return False
#     else:
#         return True


# count = 0
# for i in range(1, m):
#     if check_node(i):
#         count += 1

# print(count)
# -----------------------------------------------------------------

""" Test case
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""