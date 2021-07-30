# 외벽 점검
from itertools import permutations


def solution(n, weak, dist):
    # 원형 배열을 일자로 늘리기
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1
    # 균열의 처음부터 순차적으로 탐색
    for start in range(length):
        # 친구들로 나올 수 있는 경우의 수를 모두 확인
        for friend_cases in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friend_cases[count - 1]
            # 균열의 시작점부터 친구를 세워서 확인(시작점부터 균열 개수인 5개)
            for i in range(start, start + length):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + friend_cases[count - 1]
            # 지금까지 확인한 최소 친구 수보다 작으면 count 삽입
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1    
    return answer


n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

print(solution(n, weak, dist))