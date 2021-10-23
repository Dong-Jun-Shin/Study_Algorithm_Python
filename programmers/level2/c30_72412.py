# 순위 검색
# 문제 접근 방법과 bit를 이용한 풀이
# https://github.com/yuneg11/Programmers-Solutions/tree/master/solutions/72412%20-%20%EC%88%9C%EC%9C%84%20%EA%B2%80%EC%83%89#%EC%A1%B0%EA%B1%B4-%ED%99%95%EC%9D%B8

# defaultdict와 bisect를 이용한 풀이
from collections import defaultdict
import bisect


def get_cnt(arr, val):
    left_idx = bisect.bisect_left(arr, val)
    return len(arr) - left_idx


def solution(infos, querys):
    answer = []
    case_list = defaultdict(list)
    for info in infos:
        data = info.split()
        for a in [data[0], '-']:
            for b in [data[1], '-']:
                for c in [data[2], '-']:
                    for d in [data[3], '-']:
                        case_list[''.join([a, b, c, d])].append(int(data[4]))

    for key in case_list:
        case_list[key].sort()

    for query in querys:
        data = query.replace(' and ', ' ').split()
        key = ''.join(data[:4])
        val = int(data[4])
        answer.append(get_cnt(case_list[key], val))
    return answer


# filter를 이용한 풀이 (효율성 X)
# def solution(infos, querys):
#     answer = []
#     infos = [dict(zip(list(range(5)), info.split())) for info in infos]

#     for query in querys:
#         query = query.replace(' and ', ' ').split()
#         filters = []
#         filters.append(lambda x:x[0] == query[0] or '-' == query[0])
#         filters.append(lambda x:x[1] == query[1] or '-' == query[1])
#         filters.append(lambda x:x[2] == query[2] or '-' == query[2])
#         filters.append(lambda x:x[3] == query[3] or '-' == query[3])
#         filters.append(lambda x:int(x[4]) >= int(query[4]))

#         f_list = filter(lambda info:all(f(info) for f in filters), infos)
#         f_list = list(f_list)
#         answer.append(len(f_list))
#     return answer


infos = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
querys = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(infos, querys))
