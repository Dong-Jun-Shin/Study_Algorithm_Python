import heapq

# 무지의 먹방 라이브
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    timeList = []
    for i in range(len(food_times)):
        heapq.heappush(timeList, (food_times[i], i))

    length = len(food_times)
    preTime = 0
    while timeList:
        time = heapq.heappop(timeList)
        cycle = time[0] - preTime
        cycleTime = cycle * length
        if k < cycleTime:
            heapq.heappush(timeList, time)
            break
        else:
            k -= cycleTime
            length -= 1
            preTime += cycle

    timeList = sorted(timeList, key=lambda x: x[1])
    answer = timeList[k % length][1] + 1
        
    return answer

food_times = [4,2,3,6,7,1,5,8]
k = 16

print(solution(food_times, k))