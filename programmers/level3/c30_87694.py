# 아이템 줍기
# BFS를 이용해서, 풀이
# 사각형을 모두 겹쳐서 만든 후, 시작 지점부터 1인 곳만 방문해서, 테두리인지 체크
from collections import deque


def is_corner(graph, y, x):
    # 1이 아니면 True
    if graph[y][x] != 1: 
        return False
    for ny in range(y - 1, y + 2):
        for nx in range(x - 1, x + 2):
            # 0일 경우 True
            if graph[ny][nx] == 0: 
                return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * (51 * 2) for _ in range(51 * 2)]
    for rec_x1, rec_y1, rec_x2, rec_y2 in rectangle:
        for ny in range(rec_y1 * 2, rec_y2 * 2 + 1):
            for nx in range(rec_x1 * 2, rec_x2 * 2 + 1):
                graph[ny][nx] = 1
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    start = (characterY * 2, characterX * 2)
    q = deque([start])
    # 시작은 0이지만, visited 구분을 위해 2로 설정
    graph[start[0]][start[1]] = 2
    while q:
        y, x = q.popleft()
        for direction in directions:
            next_y = y + direction[0]
            next_x = x + direction[1]
            if is_corner(graph, next_y, next_x):
                graph[next_y][next_x] = graph[y][x] + 1
                q.append((next_y, next_x))
    # 설정했던 2를 차감
    return (graph[itemY * 2][itemX * 2] - 2) // 2


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
