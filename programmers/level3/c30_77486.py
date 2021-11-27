# 다단계 칫솔 판매
# 사전형, 재귀 사용
# 중복 seller일 경우 고려
# 사전형의 빈값은 None으로 체크

# 각 판매원의 이름을 담은 배열 enroll
# 각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열 referral
# 판매량 집계 데이터의 판매원 이름을 나열한 배열 seller
# 판매량 집계 데이터의 판매 수량을 나열한 배열 amount
answer = None
group = None
sell_datas = None


def divide(seller, benefit):
    global answer, group, sell_datas
    if seller == '-' or benefit < 1:
        return
    div_fit = benefit // 10
    answer[seller] += benefit - div_fit
    divide(group[seller], div_fit)


def solution(enroll, referral, sellers, amounts):
    global answer, group, sell_datas
    answer = dict(zip(enroll, [0] * len(enroll)))
    group = dict(zip(enroll, referral))
    sell_datas = dict(zip(sellers, [0] * len(amounts)))
    for seller, amount in zip(sellers, amounts):
        divide(seller, amount * 100)
    return list(answer.values())


enroll = ["john"]
referral = ["-"]
sellers = ["john", "john"]
amounts = [10, 15]
print(solution(enroll, referral, sellers, amounts))
