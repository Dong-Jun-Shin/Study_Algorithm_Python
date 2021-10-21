# 수식 최대화
# eval() : 문자열식을 연산해서 결과 반환(함수도 가능)
# 식을 쪼개서 우선순위대로 ()를 추가하는 알고리즘
# 정규식 표현으로 문자열식을 분리 : re.split(r'(\D)',)
from itertools import permutations

def solution(expression):
    answer = []
    opers = ['+', '-', '*']
    cases = list(permutations(opers, len(opers)))
    for case in cases:
        first = case[0]
        second = case[1]
        temp_list = []
        for exp1 in expression.split(first):
            temp = [f'({exp2})' for exp2 in exp1.split(second)]
            temp_list.append(f'({second.join(temp)})')
        answer.append(abs(eval(first.join(temp_list))))
    return max(answer)


# from itertools import permutations
# import copy
# import re


# def solution(expression):
#     answer = 0
#     # \D : 숫자 이외의 문자마다 분할
#     a = re.split(r'(\D)', expression)
#     numbers = list(map(int, expression.replace('-', ' ').replace('+', ' ').replace('*', ' ').split()))
#     for num in numbers:
#         expression = expression.replace(str(num), ' ', 1)
#     opers = list(expression.split())
#     # oper_rank [x for x in ['*','+','-'] if x in expression] // 13 ~ 19번 대체 코드
#     oper_rank = []
#     if '+' in expression:
#         oper_rank.append('+')
#     if '-' in expression:
#         oper_rank.append('-')
#     if '*' in expression:
#         oper_rank.append('*')
#     cases = list(permutations(oper_rank, len(oper_rank)))
#     for case in cases:
#         copy_numbers = copy.deepcopy(numbers)
#         copy_opers = copy.deepcopy(opers)
#         for oper in case:
#             while oper in copy_opers:
#                 for i in range(len(copy_opers)):
#                     if copy_opers[i] == oper:
#                         sum_val = 0
#                         if copy_opers[i] == '+':
#                             sum_val = copy_numbers[i] + copy_numbers[i + 1]
#                         elif copy_opers[i] == '*':
#                             sum_val = copy_numbers[i] * copy_numbers[i + 1]
#                         elif copy_opers[i] == '-':
#                             sum_val = copy_numbers[i] - copy_numbers[i + 1]
#                         copy_numbers[i] = sum_val
#                         del copy_numbers[i + 1]
#                         del copy_opers[i]
#                         break
#         answer = max(answer, abs(copy_numbers[0]))
#     return answer


expression = "177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"
print(solution(expression))
