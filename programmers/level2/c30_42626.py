# 더 맵게
# heapq는 pop이던 push를 한 후, 매번 나머지를 최소 힙에 맞춰 정렬
# 정렬이 안된 리스트는 heappush로 삽입하거나 sort로 정렬한 후, 사용
import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    first = heapq.heappop(scoville)
    while first < K:
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        sum_scov = first + (second * 2)
        heapq.heappush(scoville, sum_scov)
        first = heapq.heappop(scoville)
        answer += 1
    return answer

scoville = [9, 3, 1, 2, 10, 12]
K = 7
print(solution(scoville, K))
