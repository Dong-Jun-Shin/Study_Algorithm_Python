# 인구 이동 (인구 이동시키는 연산을 큐에서 돌 때, 한번에 작업해야 시간제한을 만족함)
from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(x, y):
    alliance = [(x, y)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    summary = graph[x][y]
    count = 1
    while q: 
        row, col = q.popleft()
        for direction in directions:
            x, y = direction
            next_row = row + x
            next_col = col + y
            if 0 > next_row or next_row >= n or 0 > next_col or next_col >= n:
                continue
            if visited[next_row][next_col] == 0 and (l <= abs(graph[row][col] - graph[next_row][next_col]) <= r):
                q.append((next_row, next_col))
                visited[next_row][next_col] = 1
                summary += graph[next_row][next_col]
                count += 1
                alliance.append((next_row, next_col))
    for i, j in alliance:
        graph[i][j] = summary // count
    return count

total_count = 0
move_count = 0
while True:
    visited = [[0] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                # 1. L이상 R이하의 인구차가 나는 나라를 모두 탐색하고 좌표와 개수를 리스트에 넣기
                bfs(i, j)
                index += 1

    # 3. 리스트가 0이면, 멈추고, 인구 이동 횟수 반환
    if index == n * n:
        break

    # 4. 인구 이동 횟수 카운트 1
    total_count += 1

print(total_count)


# ------------------------------------------------------------------- me
# from collections import deque

# n, l, r = map(int, input().split())
# graph = [[] * n for _ in range(n)]
# for i in range(n):
#     graph[i] = list(map(int, input().split()))


# def bfs(i, j):
#     q = deque()
#     q.append((i, j))
#     alliance = [(i, j)]
#     while q: 
#         row, col = q.popleft()
#         directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         for direction in directions:
#             x, y = direction
#             next_row = row + x
#             next_col = col + y
#             if 0 > next_row or next_row >= n or 0 > next_col or next_col >= n:
#                 continue
#             elif visited[next_row][next_col] == 0 and (l <= abs(graph[row][col] - graph[next_row][next_col]) <= r):
#                 q.append((next_row, next_col))
#                 alliance.append((next_row, next_col))
#         visited[row][col] = 1
#     if len(alliance) >= 2:
#         # 2. 인구이동 시키기
#         move_people(alliance)
#         return 1
#     return 0

# def move_people(alliance):
#     sum_val = 0
#     for country in alliance:
#         sum_val += graph[country[0]][country[1]]
#     sum_val = int(sum_val / len(alliance))

#     # 해당 좌표들에 결과값 넣기
#     for country in alliance:
#         graph[country[0]][country[1]] = sum_val

# result = 0
# while True:
#     move_bool = 0
#     visited = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if visited[i][j] == 0:
#                 # 1. L이상 R이하의 인구차가 나는 나라를 모두 탐색하고 좌표와 개수를 리스트에 넣기
#                 move_bool += bfs(i, j)

#     # 3. 리스트가 0이면, 멈추고, 인구 이동 횟수 반환
#     if move_bool == 0:
#         break

#     # 4. 인구 이동 횟수 카운트 1
#     result += 1


# print(result)
# ----------------------------------------------------------------------