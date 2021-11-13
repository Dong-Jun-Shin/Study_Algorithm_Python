# 보석 쇼핑
# set과 dict를 이용한 슬라이딩 윈도우 구현
from collections import defaultdict


def solution(gems):
    length = len(gems)
    kind_length = len(set(gems))
    gems_cnt = defaultdict(int)
    answer = [0, length]
    lo, hi = 0, -1
    # lo나 hi 인덱스가 넘어서면 종료
    while lo < length and hi < length:
        # 현재 보석 종류가 충분한지 확인
        if len(gems_cnt) == kind_length:
            # 보석을 가지고 있는 범위가 더 짧은 범위인지 확인
            if answer[1] - answer[0] > hi - lo:
                # 인덱스는 0부터, 진열대는 1부터이기 때문에 인덱스에 1을 더해줌
                answer[0] = lo + 1
                answer[1] = hi + 1
            # 가능 범위를 찾았으니 lo를 증가해서 맨 앞 보석 제거하고 다시 확인
            gems_cnt[gems[lo]] -= 1
            if gems_cnt[gems[lo]] == 0:
                gems_cnt.pop(gems[lo])
            lo += 1
        # 충분하지 않으면, hi 인덱스를 늘려서 보석 추가
        else:
            hi += 1
            if hi < length:
                gems_cnt[gems[hi]] += 1
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))
