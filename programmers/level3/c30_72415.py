# 카드 짝 맞추기
from collections import defaultdict, deque
from itertools import permutations, product


def get_ctrl_codi_list(card_codi_list, n, x, y):
    ctrl_codi_list = []
    for i in range(x - 1, -1, -1):
        if (i, y) in card_codi_list:
            ctrl_codi_list.append((i, y))
            break
    else:
        ctrl_codi_list.append((0, y))
    for i in range(y + 1, n):
        if (x, i) in card_codi_list:
            ctrl_codi_list.append((x, i))
            break
    else:
        ctrl_codi_list.append((x, n - 1))
    for i in range(x + 1, n):
        if (i, y) in card_codi_list:
            ctrl_codi_list.append((i, y))
            break
    else:
        ctrl_codi_list.append((n - 1, y))
    for i in range(y - 1, -1, -1):
        if (x, i) in card_codi_list:
            ctrl_codi_list.append((x, i))
            break
    else:
        ctrl_codi_list.append((x, 0))
    return ctrl_codi_list

def dijkstra(dp, board, card_codi_list, start, end):
    n = len(board)
    s_x, s_y = start
    e_x, e_y = end

    # 시작 지점에서 도착 지점까지의 최소 거리 구하기
    dist = [[int(1e9)] * n for _ in range(n)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dist[s_x][s_y] = 0     
    q = deque([(s_x, s_y, 0)])
    while q:
        x, y, cost = q.popleft()
        if x == e_x and y == e_y:
            dp[((s_x, s_y), (e_x, e_y))] = dist[e_x][e_y]
            return dist[e_x][e_y]
        # 현재 컨트롤 이동이 가능한지 판단, 이동했으면 1카운트
        ctrl_codi_list = get_ctrl_codi_list(card_codi_list, n, x, y)
        for codi in ctrl_codi_list:
            # 현재 이동된 현재 위치와 카운트한 비용을 큐에 추가
            if dist[codi[0]][codi[1]] > cost + 1:
                dist[codi[0]][codi[1]] = cost + 1
                q.append((codi[0], codi[1], cost + 1))
        # 한 칸 이동
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            # 한 칸 이동 후, 1카운트
            if dist[nx][ny] > cost + 1:
                dist[nx][ny] = cost + 1
                q.append((nx, ny, cost + 1))

def solution(board, r, c):
    n = len(board)
    card_codi_dict = defaultdict(list)
    card_codi_list = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                card_codi_dict[board[i][j]].append((board[i][j], i, j))
                card_codi_list.append((i, j))
    keys = card_codi_dict.keys()
    # Enter 횟수
    answer = len(keys) * 2
    min_dist = int(1e9)
    # 카드를 없애는 순서 순열
    for case in permutations(keys, len(keys)):
        dp = defaultdict(int)
        schedule_list = []
        for key in case:
            schedule_list.append(card_codi_dict[key])
        # 카드를 지울 수 있는 경우에 대해 하나씩 선택한 데카르트 곱
        for course in product(*schedule_list):
            # 해당 case에서 총 이동 횟수
            dist = 0
            s_x, s_y = r, c
            card_list = card_codi_list[:]
            for key, e_x, e_y in course:
                # 이전 위치 > 지금 카드 시작 위치
                if ((s_x, s_y), (e_x, e_y)) in dp:
                    dist += dp[((s_x, s_y), (e_x, e_y))]
                else:
                    dist += dijkstra(dp, board, card_list, (s_x, s_y), (e_x, e_y))
                s_x, s_y = e_x, e_y
                another = card_codi_dict[key][:]
                another.remove((key, e_x, e_y))
                key, e_x, e_y = another[0]

                # 지금 카드 시작 위치 > 지금 카드 끝 위치
                if ((s_x, s_y), (e_x, e_y)) in dp:
                    dist += dp[((s_x, s_y), (e_x, e_y))]
                else:
                    dist += dijkstra(dp, board, card_list, (s_x, s_y), (e_x, e_y))
                card_list.remove((s_x, s_y))
                card_list.remove((e_x, e_y))
                s_x, s_y = e_x, e_y
            min_dist = min(min_dist, dist)
    return answer + min_dist


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
print(solution([[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], 0, 0))
