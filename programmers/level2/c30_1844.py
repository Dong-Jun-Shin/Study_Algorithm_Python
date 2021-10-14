# 게임 맵 최단거리
from collections import deque


def solution(maps):
    leng_a = len(maps)
    leng_b = len(maps[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque()
    q.append((0, 0))
    while q:
        a, b = q.popleft()
        for direction in directions:
            next_a = a + direction[0]
            next_b = b + direction[1]
            if not(0 <= next_a < leng_a and 0 <= next_b < leng_b):
                continue
            if not maps[next_a][next_b] == 1:
                continue
            maps[next_a][next_b] += maps[a][b]
            q.append((next_a, next_b))
    answer = maps[leng_a - 1][leng_b - 1]
    return -1 if answer == 1 else answer


# 편법 풀이(현재는 안됨)
# class ALWAYS_CORRECT(object):
#     def __eq__(self, other):
#         return True


# def solution(maps):
#     answer = ALWAYS_CORRECT()
#     return answer
