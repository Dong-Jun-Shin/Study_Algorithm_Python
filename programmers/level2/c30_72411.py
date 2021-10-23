# 메뉴 리뉴얼
# collections의 Counter를 이용하면 간결하게 할 수 있음
# orders의 원소마다 메뉴가 포함된 경우, 
#    최대 20번까지 동일 메뉴가 나올 수 있음
#    이를 고려하지 않으면, 인덱스 초과 예외 발생
from itertools import combinations
from collections import Counter

#Counter 활용
def solution(orders, course):
    answer = []
    for length in course:
        cases = []
        for order in orders:
            cases += list(combinations(sorted(order), length))
        menu_list = Counter(cases).most_common()
        answer += [menu for menu, cnt in menu_list if cnt > 1 and cnt == menu_list[0][1]]
    answer = [''.join(menu) for menu in sorted(answer)]
    return answer


# 내 풀이
# from itertools import combinations

# def solution(orders, course):
#     answer = []
#     array = {}
#     for order in orders:
#         order = ''.join(sorted(order))
#         for cnt in course:
#             cases = list(combinations(order, cnt))
#             for case in cases:
#                 string = ''.join(case)
#                 if string in array:
#                     array[string] += 1
#                 else:
#                     array[string] = 1
#     array = list(array.items())
#     menus = [[[] for _ in range(21)] for _ in range(11)]
#     for menu, cnt in array:
#         if cnt > 1:
#             menus[len(menu)][cnt].append(menu)
#     for length in course:
#         for menu_list in menus[length][::-1]:
#             if menu_list:
#                 for menu in menu_list:
#                     answer.append(menu)
#                 break
#     answer.sort()
#     return answer


orders = ["ABCDE", "AB", "CDAB", "ABDE", "XABYZ", "ABXYZ", "ABCD", "ABCDE", "ABCDE", "ABCDE", "AB", "AB", "AB", "AB", "AB", "AB", "AB", "AB", "AB", "AB"]
course = [2]
print(solution(orders, course))
