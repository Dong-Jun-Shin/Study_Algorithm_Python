# 치킨 배달(순서가 바뀌어도 결과에 영향이 없으므로 조합)
from itertools import combinations


def get_sum(location_home, case):
    result = 0
    for x1, y1 in location_home:
        temp = int(1e9)
        for x2, y2 in case:
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

cases = combinations(location_chicken, m)
result = int(1e9)
for case in cases:
    result = min(result, get_sum(location_home, case))

print(result)
