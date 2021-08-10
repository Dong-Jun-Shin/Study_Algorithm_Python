# 무지의 먹방 라이브
# (사이클 이후 k번째 꺼낼 때 % 처리 - 남은 음식이 k보다 적은 경우)
# (-1 처리 - 남은 음식 개수가 0이 될 때, 큐에서 꺼내는 경우)
import heapq


def solution(food_times, k):
    q = []
    len_foods = len(food_times)
    for i in range(len_foods):
        heapq.heappush(q, (food_times[i], i))
    
    cycle = 0
    while True:
        if len_foods <= 0:
            return -1
        time, idx = heapq.heappop(q)
        cycle_val = (time - cycle) * len_foods
        if k < cycle_val:
            heapq.heappush(q, (time, idx))
            break
        k -= cycle_val
        cycle = time
        len_foods -= 1

    answer = 0
    q.sort(key=lambda x:x[1])
    time, idx = q[k % len_foods]
    answer = idx + 1

    return answer


food_times = [1, 1, 1, 1, 0]
k = 7
print(solution(food_times, k))