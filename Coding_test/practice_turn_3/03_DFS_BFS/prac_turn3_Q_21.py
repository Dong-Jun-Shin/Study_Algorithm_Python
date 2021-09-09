# 인구 이동
from collections import deque

n, input_l, input_r = map(int, input().split())
nation = []
for _ in range(n):
    nation.append(list(map(int, input().split())))

day_cnt = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while True:
    unity_list = []
    total_list = []
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            total = 0
            unity = set()
            q = deque()
            q.append((r, c))
            while q:
                i, j = q.popleft()
                for direction in directions:
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    if not (0 <= next_i < n and 0 <= next_j < n) or visited[next_i][next_j]:
                        continue
                    if input_l <= abs(nation[i][j] - nation[next_i][next_j]) <= input_r:
                        visited[next_i][next_j] = True
                        unity.add((next_i, next_j))
                        total += nation[next_i][next_j]
                        q.append((next_i, next_j))
            if unity:
                unity_list.append(unity)
            if total != 0:
                total_list.append(total)
    if len(unity_list) == 0:
        break
    for idx in range(len(unity_list)):
        avg = int(total_list[idx] / len(unity_list[idx]))
        for i, j in unity_list[idx]:
            nation[i][j] = avg
    day_cnt += 1

print(day_cnt)
