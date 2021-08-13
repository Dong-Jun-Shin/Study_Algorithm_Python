# 인구 이동
from collections import deque

n, l, r = map(int, input().split())
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

day = 0
while True:
    visited = [[False] * n for _ in range(n)]
    united = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                sum_people = country[i][j]
                move_country = set()
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for direction in directions:
                        nx = x + direction[0]
                        ny = y + direction[1]
                        if 0 > nx or nx >= n or 0 > ny or ny >= n or visited[nx][ny] == True:
                            continue

                        if l <= abs(country[x][y] - country[nx][ny]) <= r:
                            visited[nx][ny] = True
                            sum_people += country[nx][ny]
                            move_country.add((x, y))
                            move_country.add((nx, ny))
                            q.append((nx, ny))
                if len(move_country) > 0:
                    united.append((list(move_country), sum_people))

    if len(united) == 0:
        break

    for move_country, sum_people in united:
        length = len(move_country)
        for x, y in move_country:
            country[x][y] = int(sum_people / length)
    day += 1

print(day)
