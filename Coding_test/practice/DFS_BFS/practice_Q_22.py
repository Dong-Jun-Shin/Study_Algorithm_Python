# 블록 이동하기(BFS, set, 해당 좌표에서 이동할 수 있는 경우의 수를 체크)
# 회전에 의한 중복 위치가 생기는 것을 방지하기 위해 set을 사용
#     ({(1, 1), (1, 2)} == {(1, 2), (1, 1)})
# visited를 체크하기 위해, 튜플로 위치 좌표를 묶어서 추가 및 체크
from collections import deque


def get_next_codi(codi, new_board):
    next_codi = []
    codi = list(codi)
    x1, y1, x2, y2 = codi[0][0], codi[0][1], codi[1][0], codi[1][1]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for direction in directions:
        next_x1 = x1 + direction[0]
        next_y1 = y1 + direction[1]
        next_x2 = x2 + direction[0]
        next_y2 = y2 + direction[1]
        if new_board[next_x1][next_y1] == 0 and new_board[next_x2][next_y2] == 0:
            next_codi.append({(next_x1, next_y1), (next_x2, next_y2)})
    
    if x1 == x2:
        for i in [-1, 1]:
            if new_board[x1 + i][y1] == 0 and new_board[x2 + i][y2] == 0:
                next_codi.append({(x1, y1), (x1 + i, y1)})
                next_codi.append({(x2, y2), (x2 + i, y2)})
    elif y1 == y2:
        for i in [-1, 1]:
            if new_board[x1][y1 + i] == 0 and new_board[x2][y2 + i] == 0:
                next_codi.append({(x1, y1), (x1, y1 + i)})
                next_codi.append({(x2, y2), (x2, y2 + i)})

    return next_codi

def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    
    codi = {(1, 1), (1, 2)}
    visited = [codi]
    q.append((codi, 0))
    while q:
        codi, cost = q.popleft()
        if (n, n) in codi:
            return cost
        for next_codi in get_next_codi(codi, new_board):
            if next_codi not in visited:
                q.append((next_codi, cost + 1))
                visited.append(next_codi)

    return answer


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
