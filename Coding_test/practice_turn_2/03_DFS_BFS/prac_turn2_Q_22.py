# 블록 이동하기
from collections import deque


def get_next_codi(codi, board):
    next_codi = []
    codi = list(codi)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x1 = codi[0][0]
    y1 = codi[0][1]
    x2 = codi[1][0]
    y2 = codi[1][1]
    for direction in directions:
        nx1 = x1 + direction[0]
        ny1 = y1 + direction[1]
        nx2 = x2 + direction[0]
        ny2 = y2 + direction[1]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_codi.append({(nx1, ny1), (nx2, ny2)})

    if x1 == x2:
        for i in [-1, 1]:
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_codi.append({(x1 + i, y1), (x1, y1)})
                next_codi.append({(x2 + i, y2), (x2, y2)})
    else:
        for i in [-1, 1]:
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_codi.append({(x1, y1 + i), (x1, y1)})
                next_codi.append({(x2, y2 + i), (x2, y2)})
    return next_codi

def board_init(board):
    length = len(board)
    new_board = [[1] * (length + 2) for _ in range(length + 2)]
    for i in range(length):
        for j in range(length):
            new_board[i + 1][j + 1] = board[i][j]
    return new_board

def solution(board):
    n = len(board)
    board = board_init(board)
    visited = []

    start = {(1, 1), (1, 2)}
    q = deque()
    q.append((start, 0))
    visited.append(start)
    while q:
        codi, cost = q.popleft()
        if (n, n) in codi:
            return cost
        for next_codi in get_next_codi(codi, board):
            if next_codi not in visited:
                q.append((next_codi, cost + 1))
                visited.append(next_codi)
    return 0


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))