# 치킨 배달
from itertools import combinations

n, m = map(int, input().split())
graph = []
home_codi = []
chicken_codi = []
for i in range(n):
    datas = list(map(int, input().split()))
    graph.append(datas)
    for j in range(len(datas)):
        if datas[j] == 1:
            home_codi.append((i, j))
        elif datas[j] == 2:
            chicken_codi.append((i, j))

result = int(1e9)
cases = list(combinations(chicken_codi, m))
for case in cases:
    sum_dist = 0
    for h_codi in home_codi:
        min_c_dist = int(1e9)
        for c_codi in case:
            c_dist = abs(h_codi[0] - c_codi[0]) + abs(h_codi[1] - c_codi[1])
            min_c_dist = min(min_c_dist, c_dist)
        sum_dist += min_c_dist
    result = min(result, sum_dist)

print(result)
