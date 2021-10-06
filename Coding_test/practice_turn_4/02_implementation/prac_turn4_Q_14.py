# 외벽 점검
from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    
    for i in range(length):
        weak.append(weak[i] + n)
    cases = permutations(dist)

    for case in cases:
        for start in range(length):
            p_cnt = 1
            position = weak[start] + case[p_cnt - 1]
            for i in range(start, start + length):
                if  position < weak[i]:
                    p_cnt += 1
                    if p_cnt > len(case):
                        break
                    position = weak[i] + case[p_cnt - 1]
            answer = min(answer, p_cnt)

    if answer > len(dist):
        return -1
    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
