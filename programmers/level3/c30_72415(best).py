# 카드 짝 맞추기
from collections import deque
from itertools import permutations


def ctrl_move(board, x, y, dx, dy):
    n = len(board)
    for i in range(1, n):
        if 0 <= (nx := x + dx * i) < n and 0 <= (ny := y + dy * i) < n:
            if board[nx][ny] > 0:
                return (nx, ny)
            l = i
    return (x + dx * l, y + dy * l)


def move(board, start, end):
    n = len(board)
    # 시작 지점에서 도착 지점까지의 최소 거리 구하기
    dist_map = [[int(1e9)] * n for _ in range(n)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque([(start, 0)])
    while q:
        [x, y], dist = q.popleft()
        if dist < dist_map[x][y]:
            dist_map[x][y] = dist
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    q.append(((nx, ny), dist + 1))
                    q.append((ctrl_move(board, x, y, dx, dy), dist + 1))
    return dist_map[end[0]][end[1]]

def solution(board, r, c):
    n = len(board)
    card_codi_dict = {key: [] for key in range(1, 7)}
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                card_codi_dict[board[i][j]].append((i, j))
    min_dist = int(1e9)
    # 카드를 없애는 순서 순열
    for case in permutations(filter(lambda x:x, card_codi_dict.values())):
        sum_dist = 0
        codis = [(r, c)]
        copy_board = [[val for val in row] for row in board]
        # 카드짝을 순서대로 최소 거리 구한 후, 처리
        for codi_1, codi_2 in case:
            # codis에서 출발해서 해당 카드짝으로 순회하는 경우를 모두 구하기
            dist_cases = [((move(copy_board, codi, codi_1) + move(copy_board, codi_1, codi_2)), codi_2) for codi in codis]\
                        + [((move(copy_board, codi, codi_2) + move(copy_board, codi_2, codi_1)), codi_1) for codi in codis]
            # 짝 맞는 카드 처리
            copy_board[codi_1[0]][codi_1[1]] = copy_board[codi_2[0]][codi_2[1]] = 0
            # 엔터 키 2번과 가장 짧은 이동 횟수를 합산
            sum_dist += 2 + (min_case_dist := min(dist_cases)[0])
            # 가장 짧은 거리로 이동 후, 도착 좌표의 경우의 수를 시작 좌표로 설정
            codis = [case_codi for case_dist, case_codi in dist_cases if min_case_dist == case_dist]
        min_dist = min(min_dist, sum_dist)
    return min_dist


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
print(solution([[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], 0, 0))
