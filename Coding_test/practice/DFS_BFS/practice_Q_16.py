# 연구소
import copy
n, m = map(int, input().split())
graph = []
compare_graph = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

max_safe_zone = 0


# DFS를 이용해서 바이러스가 사방에 퍼지도록 재귀 수행
def virus(x, y):
    for i in range(4):
        next_x = x + directions[i][0]
        next_y = y + directions[i][1]
        if (0 > next_x or next_x >= n) or (0 > next_y or next_y >= m):
            continue
        if compare_graph[next_x][next_y] == 0:
            compare_graph[next_x][next_y] = 2
            virus(next_x, next_y)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if compare_graph[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global max_safe_zone
    global compare_graph
    # 울타리가 3개 설치된 경우
    if count == 3:
        compare_graph = copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                if compare_graph[i][j] == 2:
                    virus(i, j)
        max_safe_zone = max(max_safe_zone, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1


dfs(0)
print(max_safe_zone)

# --------------------------------------------------------------------------me
# from itertools import permutations
# from collections import deque
# import copy

# n, m = map(int, input().split())
# graph = [[] * m for _ in range(n)]

# location_empty = []
# location_virus = []
# for x in range(n):
#     data = list(map(int, input().split()))
#     graph[x] = data
#     for y in range(len(data)):
#         if data[y] == 0:
#             location_empty.append((x, y))
#         if data[y] == 2:
#             location_virus.append((x, y))
# directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# def bfs(graph):
#     safe_zone = len(location_empty) - 3
#     q = deque(location_virus)
#     while q:
#         x, y = q.popleft()
#         for direction in directions:
#             next_x = x + direction[0]
#             next_y = y + direction[1]
#             if (0 > next_x or next_x >= n) or (0 > next_y or next_y >= m):
#                 continue
#             if graph[next_x][next_y] == 0:
#                 graph[next_x][next_y] = 2
#                 q.append((next_x, next_y))
#                 safe_zone -= 1
#     return safe_zone


# max_safe_zone = 0
# for cases in list(permutations(location_empty, 3)):
#     compare_graph = copy.deepcopy(graph)
#     for case in cases:
#         compare_graph[case[0]][case[1]] = 1
#     max_safe_zone = max(max_safe_zone, bfs(compare_graph))

# print(max_safe_zone)
# ----------------------------------------------------------------------------
    