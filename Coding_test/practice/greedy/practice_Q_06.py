# 무지의 먹방 라이브(우선순위 큐, sorted(), lambda, 사이클(그리디) + 정렬을 활용)
"""
채점 결과
정확성: 42.9
효율성: 57.1
합계: 100.0 / 100.0
"""
import heapq


def solution(food_times, k):
    answer = 0
    # 전체 음식을 먹는데 필요한 시간이 장애 발생할 시간보다 적을 경우, 먹을 음식이 없으니 -1 반환
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    previous = 0                # 이전 사이클 도는데 차감한 시간(초)
    length = len(food_times)    # 현재 남아있는 음식의 개수

    while True:
        time, idx = heapq.heappop(q)
        # 이전 단계 사이클 시간(초) 차감 후, 남은 시간에 대한 사이클
        time -= previous
        n = time * length
        # 한 사이클을 도는 시간보다, 남은 시간이 많거나 같으면
        if n <= k:
            k -= n              # 남은 시간에서 사이클 시간(초)를 차감
            previous += time    # 현재 사이클 시간(초)를 누적
            length -= 1         # 남아있는 음식 개수 감소
        # 남은 시간이 적으면
        else:
            # 현재 먹으려던 음식을 큐에 삽입
            heapq.heappush(q, (time, idx))
            break

    # 남아있는 음식을 음식번호 기준으로 정렬
    q = sorted(q, key=lambda x: x[1])
    # 남아있는 횟수(초)에 해당하는 음식의 인덱스 선택 (0: 시간, 1: 음식번호)
    answer = q[k % length][1]

    return answer


"""
채점 결과
정확성: 37.5
효율성: 0.0
합계: 37.5 / 100.0
"""
# from collections import deque


# def solution(food_times, k):
#     answer = 0

#     q = deque()
#     for idx, time in enumerate(food_times, start=1):
#         q.append((idx, time))

#     for _ in range(k):
#         if not q:
#             answer = -1
#             break
#         else:
#             idx, time = q.popleft()
#             time -= 1
#             if time != 0:
#                 q.append((idx, time))

#     if q:
#         answer, time = q.popleft()

#     return answer
