# 뱀
from collections import deque

n = int(input())
graph = [[0] * (n + 2) for _ in range(n + 2)]

k_cnt = int(input())
for _ in range(k_cnt):
    x, y = map(int, input().split())
    graph[x][y] = 1

l_cnt = int(input())
oper_list = deque()
for i in range(l_cnt):
    turn_time, c = input().split()
    oper_list.append((int(turn_time), c))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_snake = 1
len_snake = 1
snake = deque()
snake_x = snake_y = 1
snake.append((snake_x, snake_y))
graph[1][1] = 2

time = 0
turn_time, c = oper_list.popleft()
while True:
    if turn_time == time:
        if c == "L":
            dir_snake = (dir_snake - 1) % len(directions)
        elif c == "D":
            dir_snake = (dir_snake + 1) % len(directions)
        if oper_list:
            turn_time, c = oper_list.popleft()
    time += 1

    next_x = snake_x + directions[dir_snake][0]
    next_y = snake_y + directions[dir_snake][1]
    if 0 < next_x < n + 1 and 0 < next_y < n + 1:
        if graph[next_x][next_y] == 1:
            len_snake += 1
        elif graph[next_x][next_y] == 2:
            break
        else:
            x, y = snake.popleft()
            graph[x][y] = 0

        snake_x, snake_y = next_x, next_y
        graph[snake_x][snake_y] = 2
        snake.append((snake_x, snake_y))
    else:
        break

print(time)
