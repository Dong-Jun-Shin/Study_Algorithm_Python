# 행렬 테두리 회전하기
def set_board(rows, columns):
    board = [[0] * columns for _ in range(rows)]
    val = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = val
            val += 1
    return board


def rotate_val(board, x1, y1, x2, y2):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    way = 1
    x, y = x1 - 1, y1 - 1
    x_diff, y_diff = x2 - x1, y2 - y1
    temp = board[x][y]
    min_value = temp
    for cnt in [y_diff, x_diff, y_diff, x_diff]:
        for _ in range(cnt):
            next_x = x + directions[way][0]
            next_y = y + directions[way][1]
            board[next_x][next_y], temp = temp, board[next_x][next_y]
            min_value = min(min_value, temp)
            x, y = next_x, next_y
        way = (way + 1) % 4
    return min_value

        
def solution(rows, columns, queries):
    answer = []
    board = set_board(rows, columns)
    for x1, y1, x2, y2 in queries:
        answer.append(rotate_val(board, x1, y1, x2, y2))
    return answer


rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))
