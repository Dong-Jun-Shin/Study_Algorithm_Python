# 기둥과 보 설치
def is_possible(answer):
    for x, y, a in answer:
        if a == 0:
            # 기둥 : 바닥 위(y == 0), 보의 한쪽 끝(x - 1, y, 1) or (x, y, 1), 다른 기둥 위(x, y - 1, 0)
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        else:
            # 보 : 기둥 위(x, y - 1, 0) or (x + 1, y - 1, 0), 양쪽 끝이 다른 보와 연결(x - 1, y, 1) and (x + 1, y, 1)
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        bulid_info = [x, y, a]
        if b == 0:
            # 삭제
            answer.remove(bulid_info)
            if not is_possible(answer):
                answer.append(bulid_info)
        else:
            # 설치
            answer.append(bulid_info)
            if not is_possible(answer):
                answer.remove(bulid_info)
    answer = sorted(answer, key=lambda x:(x[0], x[1], x[2]))
    return answer


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))
