# 블록 이동하기
from collections import deque


def get_next_codi(new_board, robot_codi):
    codi_case = []
    robot_codi = list(robot_codi)
    x1, y1 = robot_codi[0]
    x2, y2 = robot_codi[1]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for direction in directions:
        next_x_1 = x1 + direction[0]
        next_y_1 = y1 + direction[1]
        next_x_2 = x2 + direction[0]
        next_y_2 = y2 + direction[1]
        if new_board[next_x_1][next_y_1] == 0 and new_board[next_x_2][next_y_2] == 0:
            codi_case.append({(next_x_1, next_y_1), (next_x_2, next_y_2)})

    if x1 == x2:
        for i in [-1, 1]:
            if new_board[x1 + i][y1] == 0 and new_board[x2 + i][y2] == 0:
                codi_case.append({(x1, y1), (x1 + i, y1)})
                codi_case.append({(x2, y2), (x2 + i, y2)})
    elif y1 == y2:
        for i in [-1, 1]:
            if new_board[x1][y1 + i] == 0 and new_board[x2][y2 + i] == 0:
                codi_case.append({(x1, y1), (x1, y1 + i)})
                codi_case.append({(x2, y2), (x2, y2 + i)})
    return codi_case


def bfs(new_board, n):
    robot_codi = {(1, 1), (1, 2)}
    visited = []
    q = deque()
    q.append((robot_codi, 0))
    visited.append(robot_codi)
    while q:
        robot_codi, time = q.popleft()
        if (n, n) in robot_codi:
            return time
        for codi in get_next_codi(new_board, robot_codi):
            if codi not in visited:
                q.append((codi, time + 1))
                visited.append(codi)
    return 0


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    answer = bfs(new_board, n)
    return answer


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
