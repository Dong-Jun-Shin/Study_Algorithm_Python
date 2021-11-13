# 경주로 건설
from collections import deque


def solution(board):
    n = len(board)
    answer = int(1e9)
    dp = [[int(1e9) for _ in range(n)] for _ in range(n)]
    # 현재 지나간 길을 확인하기 위한 idx 추가
    directions = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]
    # i, j, cost, direction
    q = deque([(0, 0, 0, -1)])
    while q:
        i, j, cost, dir_idx = q.popleft()
        # 정답 범위이고, 현재 비용이 적을 때 값 할당
        if (i, j) == (n - 1, n - 1) and answer > cost:
            answer = cost
        for direction in directions:
            # 다음 값 셋팅
            next_i = i + direction[0]
            next_j = j + direction[1]
            add_cost = 1 if dir_idx == direction[2] or dir_idx == -1 else 6
            # 현재 값 판단할 지 여부
            if not (0 <= next_i < n and 0 <= next_j < n) or board[next_i][next_j] == 1:
                continue
            # dp[next_i][next_j] 자리에 들어갈 값에 따라 다음값이 역전되는 상황은
            # 두 수의 차가 1이상 5이하고, 먼저 꺾은 값이 다음 꺾은 값보다 더 작을 때임
            # 그래서 값이 바뀔 수 있는 상황의 차인 4를 작은 값에 빼서 역전되는 상황을 일반적인 상황으로 만듬
            # (만약 dp[next_i][next_j] 값과 들어갈 값이 같은 경우를 q에 추가하지 않는다면 5를 빼야 함)
            # (아래 조건을 넘기는 고려할 값인 상황이면, cost + add_cost가 작은 쪽이라는 전제가 생김
            #  그래서, cost + add_cost를 더 작게 만들어서 일반적인 상황으로 만듬)
            if dp[next_i][next_j] < cost + add_cost - 4:
                continue
            # dp에 값 설정 및 큐에 추가
            dp[next_i][next_j] = cost + add_cost
            q.append((next_i, next_j, cost + add_cost, direction[2]))
    return answer * 100


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))
