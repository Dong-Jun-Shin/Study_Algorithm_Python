# 무지의 먹방 라이브
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    len_food_times = len(food_times)
    loof_cnt = 0
    new_times = []
    for i in range(len_food_times):
        heapq.heappush(new_times, (food_times[i], i))
    new_times.sort()

    while new_times:
        if len_food_times == 0:
            break
        food_time, i = heapq.heappop(new_times)
        loof_time = (food_time - loof_cnt) * len_food_times
        if loof_time > k:
            heapq.heappush(new_times, (food_time, i))
            break
        len_food_times -= 1
        loof_cnt = food_time    # loof_cnt = loof_cnt + (food_time - loof_cnt)
        k -= loof_time

    new_times.sort(key=lambda x:x[1])
    
    return new_times[k % len(new_times)][1] + 1


food_times = [3, 1, 1, 1, 2, 4, 3]
k = 12
print(solution(food_times, k))