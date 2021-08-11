# 기둥과 보 설치
# x, y, 종류(0기둥, 1보), 여부(0삭제, 1설치)
def is_possible(answer):
    result = True
    for frame in answer:
        x, y, a = frame
        # 기둥
        if a == 0:
            if not (y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer):
                result = False
                break
        # 보
        else:
            if not ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):
                result = False
                break
    return result


def solution(n, build_frame):
    answer = []
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b == 0:
            answer.remove([x, y, a])
        else:
            answer.append([x, y, a])
    
        if not is_possible(answer):
            if b == 0:
                answer.append([x, y, a])
            else:
                answer.remove([x, y, a])

    # x, y, a 오름차순 정렬
    answer.sort(key=lambda x:(x[0], x[1], x[2]))

    return answer


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))
