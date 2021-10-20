# 소수 찾기
# set으로 에라토스테네스의 체 구현
# |= 합집합, -= 차집합 연산을 이용
# ** 제곱 + 0.x > 제곱근으로 이용
# from itertools import permutations


# def solution(numbers):
#     n_list = set()
#     for i in range(len(numbers)):
#         n_list |= set(map(int, map(''.join, permutations(numbers, i + 1))))
#     n_list -= set(range(0, 2))
#     for i in range(2, int(max(n_list)**0.5) + 1):
#         n_list -= set(range(i * 2, max(n_list) + 1, i))
#     print(n_list)
#     return len(n_list)


# 경우의 수를 모두 만든 다음, 각 수에 대해 소수 판단
from itertools import permutations, chain


def get_prime_cnt(cases):
    answer = 0
    for case in cases:
        if case < 2:
            continue
        for i in range(2, case // 2 + 1):
            if case % i == 0:
                break
        else:
            answer += 1
    return answer


def get_cases(numbers):
    numbers = list(map(str, numbers))
    cases = []
    for i in range(len(numbers)):
        cases.append(list(permutations(numbers, len(numbers) - i))) 
    cases = [int(''.join(s)) for s in chain(*cases)]
    cases = list(set(cases))
    cases.sort()
    return cases


def solution(numbers):
    cases = get_cases(numbers)
    answer = get_prime_cnt(cases)
    return answer


numbers = "011"
print(solution(numbers))
