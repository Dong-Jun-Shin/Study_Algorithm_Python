# 입국심사
# 시간을 기준으로 이분탐색
# 현재 기준 시간동안 심사관들이 각각 처리할 수 있는 인원 합과 목표 인원을 확인
def solution(n, times):
    answer = 0
    times.sort()
    start = 0
    end = times[-1] * n
    while start <= end:
        mid = (end + start) // 2
        count = sum([mid // time for time in times])
        if count < n:
            start = mid + 1
        elif count >= n:
            end = mid - 1
            answer = mid

    return answer


# 가장 빠른 최소값의 시간에 대해, 문제에서 명확하지 않음
# 시간 초과
# import heapq

# def solution(n, times):
#     times.sort()
#     times = list(zip([time * 2 for time in times], times))
#     answer = n if n < len(times) else len(times)
#     n -= answer
#     while n > 1:
#         next_judge, time = heapq.heappop(times)
#         heapq.heappush(times, (next_judge + time, time))
#         n -= 1

#     if n == 1:
#         times.sort(key=lambda x:x[1])
#         answer = times[0][0]


n = 6
times = [7, 10, 30]
print(solution(n, times))
