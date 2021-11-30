# 퍼즐 조각 채우기
from collections import deque


def rotate_90_degree(temp_block):
    new_block = []
    for j in range(len(temp_block[0])):
        new_block.append([temp_block[i][j] for i in reversed(range(len(temp_block)))])
    return new_block

# 블록과 빈 공간을 합쳐서 딱 맞는지 확인
def match(temp_space, temp_block, start, end):
    match_bool = True
    for i in range(len(temp_block)):
        for j in range(len(temp_block[i])):
            if start + i >= len(temp_space) or end + j >= len(temp_space[i]):
                continue
            temp_space[start + i][end + j] += temp_block[i][j]
    for i in range(len(temp_space)):
        for j in range(len(temp_space[i])):
            if temp_space[i][j] != 1:
                match_bool = False
    for i in range(len(temp_block)):
        for j in range(len(temp_block[i])):
            if start + i >= len(temp_space) or end + j >= len(temp_space[i]):
                continue
            temp_space[start + i][end + j] -= temp_block[i][j]
    return match_bool

# 블록을 빈 공간에 90도씩 돌리면서 맞는지 확인
def is_available(temp_space, temp_block):
    for _ in range(4):
        for i in range(len(temp_space)):
            for j in range(len(temp_space[i])):
                if match(temp_space, temp_block, i, j):
                    return True
        temp_block = rotate_90_degree(temp_block)
    return False

# key만큼의 길이를 가진 블록들의 좌표 리스트를 공간 배열로 모두 바꾸어서 리스트로 반환
def get_temp_list(temp_dict, key, block_val, equal):
    temp_list = []
    space_val = 1 - block_val
    for codi_list in temp_dict[key]:
        min_x = sorted(codi_list, key=lambda x:x[0])[0][0]
        min_y = sorted(codi_list, key=lambda x:x[1])[0][1]
        max_x = sorted(codi_list, key=lambda x:-x[0])[0][0]
        max_y = sorted(codi_list, key=lambda x:-x[1])[0][1]
        if equal:
            length = max(max_y - min_y + 1, max_x - min_x + 1)
            temp = [[space_val] * length for _ in range(length)]
        else:
            temp = [[space_val] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]
        for x, y in codi_list:
            temp[x - min_x][y - min_y] = block_val
        temp_list.append(temp)
    return temp_list

# 각 블록의 길이를 key로, 블록에 대한 좌표 list를 가진 딕셔너리 반환
def parse_block(board, block_val):
    n = len(board)
    temp_list = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == block_val:
                temp_list.append(bfs(board, block_val, i, j))
    temp_dict = {len(block):[] for block in temp_list}
    for codis in temp_list:
        temp_dict[len(codis)].append(codis)
    return temp_dict

# board에서 블록에 대한 좌표 리스트 반환
def bfs(board, block_val, i, j):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n = len(board)
    space_val = 1 - block_val
    codi_list = [(i, j)]
    visited = [(i, j)]
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if (nx, ny) in visited or board[nx][ny] == space_val:
                continue
            board[nx][ny] = space_val
            q.append((nx, ny))
            codi_list.append((nx, ny))
            visited.append((nx, ny))
    return codi_list

def solution(game_board, table):
    answer = 0
    # 각 블록의 길이를 key로, 블록에 대한 좌표 list를 가진 딕셔너리 반환
    space_dict = parse_block(game_board, 0)
    block_dict = parse_block(table, 1)
    # 길이별로 블록 리스트를 꺼내서 블록 하나씩 확인
    for key in block_dict:
        # key만큼의 길이를 가진 블록들의 좌표를 공간 배열로 바꾸어서 리스트로 반환
        if key not in space_dict:
            continue
        temp_block_list = deque(get_temp_list(block_dict, key, 1, False))
        temp_space_list = get_temp_list(space_dict, key, 0, True)
        # 블록의 공간 배열 리스트에서 하나씩 꺼내서 빈 공간 리스트와 비교
        while temp_block_list:
            temp_block = temp_block_list.popleft()
            for temp_space in temp_space_list:
                if is_available(temp_space, temp_block):
                    temp_space_list.remove(temp_space)
                    answer += key
                    break
    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]], [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]))
