# 외벽 점검(순서가 바뀌면 결과에 영향이 있으므로 순열)
from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    len_weak = len(weak)
    for i in range(len_weak):
        weak.append(n + weak[i])

    dist_cases = list(permutations(dist, len(dist)))
    for dist_case in dist_cases:
        for start in range(len_weak):
            count = 1
            position = weak[start] + dist_case[count - 1]
            for i in range(start, len_weak + start):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + dist_case[count - 1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1    
    return answer


n = 12
weak = [1, 2, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
