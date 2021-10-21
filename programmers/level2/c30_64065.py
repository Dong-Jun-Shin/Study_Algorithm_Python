# 튜플
# 정규식을 이용해서 리스트로 변환
# key=len 함수를 이용해서 길이 순으로 정렬
# Counter로 빈도순 정렬한 리스트를 반환
import re
from collections import Counter


def solution(s):
    s = Counter(re.findall('\d+', s)).most_common()
    return list(map(int, [k for k, v in s]))


# import re


# def solution(s):
#     answer = []
#     set_list = []
#     for n_set in re.split(r'\},\{',s[2:-2]):
#         set_list.append(list(map(int, n_set.split(','))))
#     set_list.sort(key=len)
#     for n_set in set_list:
#         for val in n_set:
#             if val not in answer:
#                 answer.append(val)
#     return answer


s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))