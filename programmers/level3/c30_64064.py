# 불량 사용자
# permutations와 모든 경우의 수를 확인하는 방법
# 마지막 경우의 수에서 순서는 상관없지만, ban_id와 user_id를 체크하는 과정에서 
#   각 자리별 ban_id 순서에 따라 id가 맞아야 하므로, permutations로 모든 경우를 고려한 뒤 중복 제거
from itertools import permutations


def ban_check(user_id, banned_id):
    for i in range(len(banned_id)):
        if len(user_id[i]) != len(banned_id[i]):
            return False
        for j in range(len(banned_id[i])):
            if banned_id[i][j] != '*' and user_id[i][j] != banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    cases = list(permutations(user_id, len(banned_id)))
    for case in cases:
        if ban_check(case, banned_id):
            answer.append(case)
    return len(list(set(map(tuple, map(sorted, map(list, answer))))))


# 데카르트 곱(product)과 문자열을 치환해서 범위로 찾는 방법(테케3 X, 테케5 시간초과)
# from collections import defaultdict
# from itertools import product
# import bisect


# def toUpper(string):
#     return string.upper()

# def get_rlist(user_list, start, end):
#     right_idx = bisect.bisect_right(user_list, end)
#     left_idx = bisect.bisect_left(user_list, start)
#     # 역순을 원래대로 복구
#     return list(map(''.join, map(reversed, user_list[left_idx: right_idx])))

# def get_list(user_list, start, end):
#     right_idx = bisect.bisect_right(user_list, end)
#     left_idx = bisect.bisect_left(user_list, start)
#     return list(user_list[left_idx: right_idx])

# def solution(user_list, banned_list):
#     # 대문자로 변환
#     user_list = list(map(toUpper, user_list))
#     banned_list = list(map(toUpper, banned_list))
#     # 길이에 따라 유저 아이디를 분류하는 dict
#     user_len_dict = defaultdict(list)
#     user_len_rdict = defaultdict(list)
#     # ban_id에 적합한 아이디를 길이에 따라 분류하는 dict
#     target_len_dict = defaultdict(set)

#     # 유저 아이디를 길이에 따라 분류하고 정렬
#     for user_id in user_list:
#         user_len_dict[len(user_id)].append(user_id)
#         user_len_rdict[len(user_id)].append(user_id[::-1])
#     for len_list in user_len_dict:
#         user_len_dict[len_list].sort()
#         user_len_rdict[len_list].sort()

#     # 유저 아이디 중에 ban_id와 적합 여부 확인 후, target_len_dict에 추가
#     process_ban_id = []
#     for ban_id in banned_list:
#         # 이미 확인된 ban_id는 제외
#         if ban_id in process_ban_id:
#             continue
#         # 0(48) ~ 9(57), A(65) ~ Z(90)
#         start = ban_id.replace('*', '0')
#         end = ban_id.replace('*', 'Z')
#         ban_list = get_list(user_len_dict[len(ban_id)], start, end)
#         rban_list = get_rlist(user_len_rdict[len(ban_id)], start[::-1], end[::-1])
#         target_len_dict[ban_id].update(ban_list if len(ban_list) < len(rban_list) else rban_list)
#         process_ban_id.append(ban_id)

#     # ban_id마다 가능한 경우들을 추가
#     cases_list = []
#     for ban_id in banned_list:
#         cases_list.append(list(target_len_dict[ban_id]))
    
#     # 경우의 수에 대해 중복을 제거 후 추가
#     cases_list = set(map(tuple, map(sorted, map(set, product(*cases_list)))))
#     cases_list = [case for case in cases_list if len(case) == len(banned_list)]
    
#     return len(cases_list)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
print(solution(["12345", "12453", "aaaaa"], ["1****", "a****" ]))
print(solution(['fradi'], ['fr*dy']))
# print(solution(["aaaaaaaa", "bbbbbbbb", "cccccccc", "dddddddd", "eeeeeeee", "ffffffff", "gggggggg", "hhhhhhhh"], ["********", "********", "********", "********", "********", "********", "********", "********"]))
