# 광고 삽입
# 구간합에 시간 기준으로 처리하는 단순 이중 for문보다 메모리제이션 처리가 빠름
# 단순 이중 for문 : 최대 (100 * 60 * 60) * 30만
# 메모리제이션 : 최대 100 * 60 * 60
def time_to_second(time):
    hour, minute, second = time.split(':')
    return (int(hour) * 60 * 60) + (int(minute) * 60) + int(second)

def second_to_time(second):
    hour = second // (60 * 60)
    second %= (60 * 60)
    minute = second // 60
    second %= 60
    return '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, second)

def solution(play_time, adv_time, logs):
    play_time = time_to_second(play_time)
    adv_time = time_to_second(adv_time)
    if play_time == adv_time:
        return second_to_time(0)

    all_times = [0 for _ in range(play_time + 1)]
    # 단순 이중 for문
    # 시간을 기준으로 한 구간 더하기
    # 100 * 60 * 60 근처의 시청 시간이 여러개면 (해당 시청 시간 * log 개수)만큼을 처리 (최대 (100 * 60 * 60) * 30만)
    # for log in logs:
    #     for i in range(time_to_second(log[:8]), time_to_second(log[9:])):
    #         all_times[i] += 1
    # DP, 메모리제이션을 활용한 코드
    # 메모리제이션을 통해, 시작과 끝값만 표시 후, all_times만큼을 처리 (최대 100 * 60 * 60)
    for log in logs:
        start_time, end_time = log.split('-')
        start_time = time_to_second(start_time)
        end_time = time_to_second(end_time)
        all_times[start_time] += 1
        all_times[end_time] -= 1
    for i in range(1, len(all_times)):
        all_times[i] = all_times[i] + all_times[i - 1]
    
    sum_val = sum(all_times[:adv_time])
    best_start_time = 0
    max_sum = sum_val
    for i in range(adv_time, play_time):
        if all_times[i - adv_time] != all_times[i]:
            sum_val -= all_times[i - adv_time]
            sum_val += all_times[i]
            if sum_val > max_sum:
                max_sum = sum_val
                best_start_time = i - adv_time + 1

    return second_to_time(best_start_time)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
