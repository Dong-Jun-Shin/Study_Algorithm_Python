# H-Index
# 논문 인용된 횟수로 보는게 아닌 0번 인용부터 순차 확인
# h번 이상 인용된 논문의 개수를 enumerate로 표현
# 자신이 인용된 횟수와 자신보다 많이 인용된 논문 갯수 중 작은 쪽을 가지게 됨
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


# 현재 h번이상인 논문을 이분탐색으로 찾아서 확인
# import bisect

# def solution(citations):
#     answer = 0
#     citations.sort()
#     for h in range(len(citations) + 1):
#         if h <= len(citations) - bisect.bisect_left(citations, h):
#             answer = max(answer, h)
#     return answer


citations = [0, 0, 0, 0, 0, 0, 0]
print(solution(citations))
