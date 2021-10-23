# 삼각 달팽이
from itertools import chain


def solution(n):
    answer = []
    graph = [[0] * n for _ in range(n)]
    x = 0
    y = -1
    val = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            graph[y][x] = val
            val += 1
    answer = [i for i in chain(*graph) if i != 0]
    return answer
