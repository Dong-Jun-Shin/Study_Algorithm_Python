# 뱀
from collections import deque

n = int(input())
graph = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(n + 2):
    graph[i][0], graph[i][n + 1] = 9, 9
    graph[0][i], graph[n + 1][i] = 9, 9

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 2

l_cnt = int(input())
turn_list = deque()
for _ in range(l_cnt):
    x, c = input().split()
    turn_list.append((int(x), c))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
graph[1][1] = 1
snake_rotation = 1
snake_x, snake_y = 1, 1
snake = deque()
snake.append((1, 1))
x_time = 0
c_turn = ''
if turn_list:
    x_time, c_turn = turn_list.popleft()

time = 0
while True:
    time += 1
    next_x = snake_x + directions[snake_rotation][0]
    next_y = snake_y + directions[snake_rotation][1]
    if graph[next_x][next_y] == 1 or graph[next_x][next_y] == 9:
        break
    
    if graph[next_x][next_y] == 0:
        pre_x, pre_y = snake.popleft()
        graph[pre_x][pre_y] = 0
    snake.append((next_x, next_y))
    graph[next_x][next_y] = 1
    snake_x, snake_y = next_x, next_y
    
    if time == x_time:
        if c_turn == 'L':
            snake_rotation -= 1
        elif c_turn == 'D':
            snake_rotation += 1
        snake_rotation %= 4
        
        if turn_list:
            x_time, c_turn = turn_list.popleft()

print(time)
