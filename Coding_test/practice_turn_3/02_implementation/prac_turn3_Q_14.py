# 외벽 점검
from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    len_weak = len(weak)
    for i in range(len_weak):
        weak.append(weak[i] + n)

    cases = list(permutations(dist, len(dist)))
    for case in cases:
        for start in range(len_weak):
            count = 1
            position = weak[start] + case[count - 1]
            for i in range(start, start + len_weak):
                if position < weak[i]:
                    count += 1
                    if count > len(case):
                        break
                    position = weak[i] + case[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
