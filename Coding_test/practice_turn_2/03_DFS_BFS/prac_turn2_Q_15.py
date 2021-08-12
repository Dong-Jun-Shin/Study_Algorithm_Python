# 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distances = [INF] * (n + 1)
distances[x] = 0

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append((e, 1))

q = deque()
q.append(x)
while q:
    start = q.popleft()
    for end, cost in graph[start]:
        if distances[end] > distances[start] + cost:
            distances[end] = distances[start] + cost
            q.append(end)

print_bool = False
string = ''
for i in range(1, len(distances)):
    if distances[i] == k:
        print_bool = True
        print(i)

if not print_bool:
    print('-1')
