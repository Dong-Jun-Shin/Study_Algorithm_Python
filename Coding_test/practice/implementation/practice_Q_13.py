# 치킨 배달
from itertools import combinations


def get_sum(case):
    result = 0
    for home in location_home:
        temp = 1e9
        x1, y1 = home
        for chicken in case:
            x2, y2 = chicken
            temp = min(temp, abs(x1 - x2) + abs(y1 - y2))
        result += temp
    return result


n, m = map(int, input().split())
graph = []
location_home = []
location_chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if data[j] == 1:
            location_home.append((i, j))
        elif data[j] == 2:
            location_chicken.append((i, j))

cases = list(combinations(location_chicken, m))

result = 1e9
for case in cases:
    result = min(result, get_sum(case))

print(result)
