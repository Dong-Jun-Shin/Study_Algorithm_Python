# 실패율
import bisect


def get_count(stages, i):
    right_idx = bisect.bisect_right(stages, i)
    left_idx = bisect.bisect_left(stages, i)
    return right_idx - left_idx


def solution(N, stages):
    answer = []
    stages.sort()
    failure = [0] * (N + 1)
    for i in range(1, N + 1):
        cnt = get_count(stages, i)
        if cnt > 0:
            idx = bisect.bisect_left(stages, i)
            people = len(stages) - idx
            failure[i] = cnt / people
    f_list = []
    for i in range(1, len(failure)):
        f_list.append((failure[i], i))
    f_list.sort(reverse=True, key=lambda x:(x[0], -x[1]))
    for failure, i in f_list:
        answer.append(i)

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
