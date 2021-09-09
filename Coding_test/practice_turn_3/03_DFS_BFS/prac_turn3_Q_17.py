# 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
graph = []
virus_codis = []
for i in range(n):
    datas = list(map(int, input().split()))
    for j in range(n):
        if datas[j] != 0:
            virus_codis.append((datas[j], i, j))
    graph.append(datas)

s, x, y = map(int, input().split())
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
time = 0
virus_codis.sort()
virus_codis.append((-1, -1, -1))
q = deque(virus_codis)
while True:
    if time >= s or not q:
        break
    virus, i, j = q.popleft()
    if i == -1 and j == -1:
        q.append((-1, -1, -1))
        time += 1
        continue
    for direction in directions:
        next_i = i + direction[0]
        next_j = j + direction[1]
        if not(0 <= next_i < n and 0 <= next_j < n):
            continue
        if graph[next_i][next_j] == 0:
            graph[next_i][next_j] = virus
            q.append((virus, next_i, next_j))

print(graph[x - 1][y - 1])
