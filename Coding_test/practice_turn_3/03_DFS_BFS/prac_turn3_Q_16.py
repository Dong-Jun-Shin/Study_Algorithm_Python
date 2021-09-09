# 연구소
from copy import deepcopy
from itertools import combinations
from collections import deque


def spread_virus(new_graph, virus_codis):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for r, c in virus_codis:
        q = deque()
        q.append((r, c))
        while q:
            i, j = q.popleft()
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if not(0 <= next_i < n and 0 <= next_j < m):
                    continue
                if new_graph[next_i][next_j] == 0:
                    new_graph[next_i][next_j] = 2
                    q.append((next_i, next_j))
    return new_graph


def simulation(graph, wall, virus_codis):
    new_graph = deepcopy(graph)
    safe_z_count = 0
    for r, c in wall:
        new_graph[r][c] = 1
    simul_graph = spread_virus(new_graph, virus_codis)
    for i in range(n):
        for j in range(m):
            if simul_graph[i][j] == 0:
                safe_z_count += 1
    return safe_z_count


n, m = map(int, input().split())
graph = []
virus_codis = []
space_codis = []
for i in range(n):
    datas = list(map(int, input().split()))
    for j in range(m):
        if datas[j] == 2:
            virus_codis.append((i, j))
        elif datas[j] == 0:
            space_codis.append((i, j))
    graph.append(datas)

max_safe_zone = 0
cases = combinations(space_codis, 3)
for case in cases:
    max_safe_zone = max(max_safe_zone, simulation(graph, case, virus_codis))

print(max_safe_zone)
