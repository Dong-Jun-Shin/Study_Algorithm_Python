# 기능개발
from collections import deque

def solution(progresses, speeds):
    answer = []
    while progresses:
        length = len(progresses)
        for i in range(length):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            cnt = 0
            new_prog = deque(progresses)
            new_speeds = deque(speeds)
            while new_prog:
                val = new_prog.popleft()
                if val >= 100:
                    cnt += 1
                else:
                    new_prog.appendleft(val)
                    break
                new_speeds.popleft()
            progresses = list(new_prog)
            speeds = list(new_speeds)
            answer.append(cnt)
    return answer

progresses = [55, 6, 65]
speeds = [5, 10, 7]
print(solution(progresses, speeds))
