# 거리두기 확인하기
from collections import deque


def is_bool(graph, p_list):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for p_x, p_y in p_list:
        visited = []
        q = deque()
        q.append((p_x, p_y, 0))
        while q:
            p_x, p_y, cnt = q.popleft()
            for direction in directions:
                next_x = p_x + direction[0]
                next_y = p_y + direction[1]
                if (next_x, next_y) in visited:
                    continue
                if not(0 <= next_x < 5 and 0 <= next_y < 5):
                    continue
                if graph[next_x][next_y] == 'P':
                    return 0
                elif graph[next_x][next_y] == 'O' and cnt == 0:
                    q.append((next_x, next_y, cnt + 1))
                    visited.append((p_x, p_y))
    return 1


def solution(places):
    answer = []
    for place in places:
        graph = []
        p_list = []
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    p_list.append((i, j))
            graph.append(list(place[i]))
        answer.append(is_bool(graph, p_list))
    return answer
    

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]
print(solution(places))