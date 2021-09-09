# 감시 피하기
from itertools import combinations
import copy


def is_avoid(new_graph, location_t):
    for codi_t in location_t:
        for i in range(codi_t[0] - 1, -1, -1):
            if new_graph[i][codi_t[1]] == "O":
                break
            elif new_graph[i][codi_t[1]] == "S":
                return False
        for i in range(codi_t[0] + 1, len(new_graph)):
            if new_graph[i][codi_t[1]] == "O":
                break
            elif new_graph[i][codi_t[1]] == "S":
                return False
        for j in range(codi_t[1] - 1, -1, -1):
            if new_graph[codi_t[0]][j] == "O":
                break
            elif new_graph[codi_t[0]][j] == "S":
                return False
        for j in range(codi_t[1] + 1, len(new_graph)):
            if new_graph[codi_t[0]][j] == "O":
                break
            elif new_graph[codi_t[0]][j] == "S":
                return False
    return True


def simulation(graph, cases, location_t):
    for case in cases:
        new_graph = copy.deepcopy(graph)
        for codi_x in case:
            new_graph[codi_x[0]][codi_x[1]] = "O"
        if is_avoid(new_graph, location_t):
            return True
    return False


n = int(input())
graph = []
location_t = []
location_x = []
for i in range(n):
    datas = list(input().split())
    for j in range(n):
        if datas[j] == "X":
            location_x.append((i, j))
        elif datas[j] == "T":
            location_t.append((i, j))
    graph.append(datas)

cases = list(combinations(location_x, 3))
if simulation(graph, cases, location_t):
    print("YES")
else:
    print("NO")
