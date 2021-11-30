# 금과 은 운반하기
# '시간 내 최대로 옮길 수 있는 양'은 필요 금, 필요 은, 필요 금 + 은의 양을 넘어야 운반 가능
# a + b <= w[i] * move_cnt((T // (t[i] * 2)) + (T % (t[i] *2)) < t[i]? 1)
# move_cnt는 왕복 가능 횟수 + 마지막 편도 횟수
def solution(a, b, g, s, w, t):
    start = 0
    # a 최대량(1e9) + b 최대량(1e9) + w가 최소인 1일 때, 최대 운반 시간 t(1e5)의 왕복
    end = int(1e9) * 2 * int(1e5) * 2
    answer = end
    while start <= end:
        mid = (start + end) // 2
        gold, silver, both = 0, 0, 0
        # 나라별 시간 내 운반 가능한 모든 경우의 최대량 구하기
        for i in range(len(t)):
            # 시간 내 운반 가능 횟수(왕복 + 편도)
            move_cnt = mid // (t[i] * 2)
            move_cnt += 1 if mid % (t[i] * 2) >= t[i] else 0
            # i번째 나라의 최대 운반량을 각각 경우에 맞게 누적
            i_max_weight = w[i] * move_cnt
            gold += min(g[i], i_max_weight)
            silver += min(s[i], i_max_weight)
            both += min(g[i] + s[i], i_max_weight)
        # 금만 다 옮겼을 때, 필요 금을 충족할 수 있고
        # 은만 다 옮겼을 때, 필요 은을 충족할 수 있고
        # 금과 은을 다 옮겼을 때, 필요 금과 은을 모두 충족할 수 있다면 해당 시간 내에 운반 가능
        if gold >= a and silver >= b and both >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
print(solution(90, 500, [70, 70, 0, 10], [0, 0, 500, 10], [100, 100, 2, 10], [4, 8, 1, 5]))
