# 뱀
from collections import deque

n = int(input())
graph = [[0] * (n + 2) for _ in range(n + 2)]
graph[0] = [9] * (n + 2)
graph[n + 1] = [9] * (n + 2)
for i in range(1, n + 1):
    graph[i][0] = 9
    graph[i][n + 1] = 9

k = int(input())
for _ in range(k):
    apple_x, apple_y = map(int, input().split())
    graph[apple_x][apple_y] = 1

l = int(input())
turn_order = deque()
for _ in range(l):
    turn_order.append((input().split()))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

time = 0
x, y = 1, 1
way = 1
graph[x][y] = 2
order = turn_order.popleft()

q = deque()
q.append((1, 1))
while True:
    if time == int(order[0]):
        way = (way - 1) % 4 if 'L' == order[1] else (way + 1) % 4
        if len(turn_order) > 0:
            order = turn_order.popleft()

    nx = x + directions[way][0]
    ny = y + directions[way][1]
    if graph[nx][ny] == 9 or graph[nx][ny] == 2:
        time += 1
        break
        
    if graph[nx][ny] != 1:
        tail = q.popleft()
        graph[tail[0]][tail[1]] = 0

    graph[nx][ny] = 2
    q.append((nx, ny))
    x, y = nx, ny

    time += 1
    
print(time)
