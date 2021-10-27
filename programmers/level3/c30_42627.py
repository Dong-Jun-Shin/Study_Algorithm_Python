# 디스크 컨트롤러
def solution(jobs):
    # 요청 순으로 정렬
    jobs.sort()
    # 유휴 상태에서 제일 빠른 요청 처리
    start, cost = jobs.pop(0)
    answer = [cost]
    next_end = start + cost
    while jobs:
        # 처리가 끝난 시점에 있는 요청을 반환
        temp = [(job[0], job[1]) for job in jobs if job[0] <= next_end]
        # 처리가 끝난 시점에 요청이 있는지 확인
        if temp:
            # 현재 요청들을 처리 시간 순으로 정렬
            temp.sort(key=lambda x: x[1])
            start, cost = temp.pop(0)
            jobs.remove([start, cost])
        else:
            # 요청 시간으로 정렬된 리스트에서 가장 빠른 다음 요청을 가져옴
            start, cost = jobs.pop(0)
            next_end = start
        # 요청이후 처리되기까지의 시간을 추가
        answer.append(next_end - start + cost)
        # 요청 처리가 끝난 시점을 next_end에 입력
        next_end += cost
    return sum(answer) // len(answer)


jobs = [[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]
print(solution(jobs))
