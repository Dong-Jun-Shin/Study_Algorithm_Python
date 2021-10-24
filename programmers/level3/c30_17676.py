# 추석 트래픽
# datatime의 strptime, timedelta를 이용해서 풀이
# 끝나는 시간에 1초를 더해서, 체크하는 순간에 리스트 개수로 파악 가능
# 종료 시간 기준이라, 시작 시간은 정렬되어 있지 않음
#   시작 시간으로 정렬을 해도 타임라인으로 표현했을 때, 체크할 때 달라지지 않음
#   그래서 시작 시간 정렬로 타임라인 로그를 모두 시작한 시점까지만 체크할 수 있음
# ! 주의 !
#   밀리초 없이 나온 경과시간은 체크해서 .0을 추가
#   경과 시간을 뺀 후, 시분초만 남으므로, 종료시간 리스트도 비교를 위해 0초를 빼서 시분초만 남김
from datetime import datetime, timedelta


def solution(lines):
    answer = 1
    s_time_list, e_time_list = [], []
    for line in lines:
        line = line.split()
        # 종료 시간을 datetime으로 변환
        e_time = datetime.strptime(line[1], '%H:%M:%S.%f')
        # 처리 시간을 datetime으로 변환
        p_time = line[2].replace('s', '')
        p_time = p_time if p_time.find('.') != -1 else p_time + '.0'
        p_time = datetime.strptime(p_time, '%S.%f')
        dump_p_time = datetime.strptime('0.0', '%S.%f')
        # 시작 시간(종료 시간 - 처리 시간 + 시작 시간 포함하기 위한 0.001초)
        s_time_list.append(e_time - p_time + timedelta(milliseconds=1))
        # 종료 시간(종료 시간 - 0초 + 초당 확인을 위한 1초)
        e_time_list.append(e_time - dump_p_time + timedelta(seconds=1))
    # 시작 지점 기준으로 확인을 위한 정렬
    s_time_list.sort()

    processing = []
    while s_time_list:
        # 처리 작업 추가
        s_time = s_time_list.pop(0)
        processing.append(e_time_list.pop(0))

        # 처리 끝난 작업 제거
        while processing:
            if s_time >= processing[0]:
                processing.pop(0)
            else:
                break

        # 현재 처리중인 양 확인
        answer = max(answer, len(processing))
    return answer


lines = ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]
print(solution(lines))
