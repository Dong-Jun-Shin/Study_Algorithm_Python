# 치킨 배달
from itertools import combinations

n, m = map(int, input().split())
graph = []
codi_home = []
codi_chicken = []
for i in range(n):
    datas = list(map(int, input().split()))
    for j in range(len(datas)):
        if datas[j] == 1:
            codi_home.append((i, j))
        elif datas[j] == 2:
            codi_chicken.append((i, j))
    graph.append(datas)

answer = int(1e9)
cases = combinations(codi_chicken, m)
for case in cases:
    case_dist = 0
    for home_x, home_y in codi_home:
        chic_dist = int(1e9)
        for chic_x, chic_y in case:
            dist = abs(home_x - chic_x) + abs(home_y - chic_y)
            chic_dist = min(chic_dist, dist)
        case_dist += chic_dist
    answer = min(answer, case_dist)

print(answer)
