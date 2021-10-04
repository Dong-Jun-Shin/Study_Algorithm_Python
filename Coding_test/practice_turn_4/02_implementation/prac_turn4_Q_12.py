# 기둥과 보 설치
def is_available(answer):
    for frame in answer:
        x, y, a = frame
        # 기둥
        if a == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
        # 보
        elif a == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
        return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # 설치
        if b == 1:
            answer.append([x, y, a])
            if not is_available(answer):
                answer.remove([x, y, a])
        # 삭제
        elif b == 0:
            answer.remove([x, y, a])
            if not is_available(answer):
                answer.append([x, y, a])
    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    return answer


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))
