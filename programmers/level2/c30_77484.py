# 로또의 최고 순위와 최저 순위
# list, .count를 활용한 풀이
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    unknown_cnt = lottos.count(0)
    hit_cnt = 0
    for num in lottos:
        if num in win_nums:
            hit_cnt += 1
    return [rank[hit_cnt + unknown_cnt], rank[hit_cnt]]


# set을 활용한 풀이
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    unknown_cnt = lottos.count(0)
    hit_cnt = len(set(lottos) & set(win_nums))
    return [rank[hit_cnt + unknown_cnt], rank[hit_cnt]]
