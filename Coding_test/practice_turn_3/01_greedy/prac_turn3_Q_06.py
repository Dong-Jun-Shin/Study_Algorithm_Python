# 무지의 먹방 라이브
import heapq


def solution(food_times, k):
    if sum(food_times) < k:
        return -1

    length = len(food_times)
    q = []
    for i in range(length):
        heapq.heappush(q, (food_times[i], i + 1))

    spend_time = 0
    while q:
        time, idx = heapq.heappop(q)
        time -= spend_time
        if time <= 0:
            length -= 1
            continue
        if k >= time * length:
            k -= time * length
            spend_time += time
            length -= 1
        else:
            heapq.heappush(q, (time, idx))
            break

    q.sort(key=lambda x: x[1])
    answer = q[k % length][1]
    return answer


food_times = [4, 1, 1, 5]
k = 4
print(solution(food_times, k))
