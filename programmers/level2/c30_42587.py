# 프린터
# any(), all() : or, and 기능을 하는 함수. 인자 리스트 중 True의 여부로 반환
# enumerate() : 인자 리스트와 그에 해당하는 idx를 반환 (idx, 인자)
def solution(priorities, location):
    answer = 0
    queue = [(i, e) for i, e in enumerate(priorities)]
    while True:
        cur_val = queue.pop(0)
        if any([cur_val[1] < target[1] for target in queue]):
            queue.append(cur_val)
        else:
            answer += 1
            if cur_val[0] == location:
                break
    return answer


# from collections import deque


# def solution(priorities, location):
#     answer = 0
#     priorities.append(0)
#     q = deque(priorities)
#     while q:
#         val = q.popleft()
#         if val >= max(q):
#             answer += 1
#             if location == 0:
#                 break
#             else:
#                 location -= 1
#         else:
#             q.append(val)
#             if location == 0:
#                 location = len(q) - 1
#             else:
#                 location -= 1
#     return answer
