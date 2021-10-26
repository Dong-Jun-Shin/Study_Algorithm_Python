# 셔틀버스
# 운행하는 버스 리스트를 만들고 현재 버스 시간에 탈 수 있는 승객들만 꺼냄
def solution(n, t, m, timetable):
    answer = 0
    timetable = sorted([int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in timetable])
    bustable = [(9 * 60) + (i * t) for i in range(n)]
    for bus_time in bustable:
        passenger = [time for time in timetable if time <= bus_time]
        psg_length = len(passenger)
        if bus_time == bustable[-1]:
            if psg_length < m:
                answer = bus_time
            elif psg_length >= m:
                answer = passenger[m - 1] - 1
        elif psg_length < m:
            timetable = timetable[psg_length:]
        elif psg_length >= m:
            timetable = timetable[m:]
    return str(answer // 60).zfill(2) + ':' + str(answer % 60).zfill(2)


# 현재 버스 시간에 맞춰서 승객을 계속 꺼내고, 다음 차에 태우고를 승객이 없을 때까지 반복
# from collections import deque
# def solution(n, t, m, timetable):
#     s_time = 9 * 60
#     e_time = s_time + ((n - 1) * t)
#     timetable = sorted([int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in timetable])
#     timetable = deque([time for time in timetable if 0 <= time <= e_time])
#     last_p_time = s_time
#     cnt = 1
#     while cnt <= n:
#         last_p_time = s_time
#         for i in range(1, m + 1):
#             if not timetable or not s_time >= timetable[0]:
#                 i -= 1
#                 break
#             last_p_time = timetable.popleft()
#         if i < m:
#             if not timetable:
#                 last_p_time = e_time
#                 break
#             else:
#                 while s_time < timetable[0]:
#                     s_time += t
#                     cnt += 1
#                 continue
#         s_time += t
#         cnt += 1
#     else:
#         last_p_time -= 1
#     answer = str(last_p_time // 60).zfill(2) + ':' + str(last_p_time % 60).zfill(2)
#     return answer
    

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1,	["23:59"]))
print(solution(10, 60, 45,	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
