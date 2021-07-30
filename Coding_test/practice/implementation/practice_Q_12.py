# # 기둥과 보 설치
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            # 기둥은 '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or ([x - 1, y, 1] in answer) or ([x, y, 1] in answer) or ([x, y - 1, 0] in answer):
                continue
            else:
                return False
        elif stuff == 1:
            # 보는 '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if ([x, y - 1, 0] in answer) or ([x + 1, y - 1, 0] in answer) or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for order in build_frame:
        x, y, stuff, operate = order
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        elif operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))

# ----------------------------------------------------------------------- me
# def solution(n, build_frame):
#     result = []

#     # 1. N x N 크기의 graph 생성하기
#     graph = [[9] * (n + 1) for _ in range(n + 1)]
#     graph[0] = [2] * (n + 1)

#     # build_frame을 y, a, b 순으로 정렬
#     build_frame = sorted(build_frame, key=lambda x: (-x[3], x[1], x[2]))

#     build_type = [[(1, 1), (1, -1), (1, 0)], [(0, 2)]]
#     # 2. 빌드 프레임에서 작업 꺼내기
#     for order in build_frame:
#         x, y, a, b = order
#         # 3. 설치인 경우
#         if b == 1:
#             # 만들 수 있는지 확인 (0: 기둥, 1: 보, 2: 가능)
#             if graph[y][x] <= 2:
#                 # 4. result.append(list) 추가
#                 graph[y][x] = a
#                 result.append([x, y, a])
                
#                 # 5. graph에 현재 좌표에서 기둥(0)이면 y += 1, x -= 1, x += 1과 보(1)이면 x += 1에서 기둥, 보 설치 가능 여부 표시
#                 for case in build_type[a]:
#                     next_y = y + case[0]
#                     next_x = x + case[1]
#                     if 0 <= next_y and next_y <= n and 0 <= next_x and next_x <= n:
#                         graph[next_y][next_x] = 2
#         # 4. 삭제인 경우
#         elif b == 0:
#             delete_bool = True
#             for case in build_type[0]:
#                 bool_list = []
#                 next_y = y + case[0]
#                 next_x = x + case[1]
#                 if 0 <= next_y and next_y <= n and 0 <= next_x and next_x <= n:
#                     if graph[next_y][next_x] < 2:
#                         bool_list.append(1)
#                     else:
#                         bool_list.append(0)
            
#             # 기둥(0)은 현재 삭제할 좌표의 y += 1의 x -= 1과 x에 보(1)가 있거나 x에 기둥(0)이 있으면 불가
#             # if (bool_list[0] + bool_list[1]) != 2 or bool_list[2] == 1:
#             #     continue
#             # 보(1)는 x -= 1과 x += 1에 보(1)가 있거나, x나 x += 1에 기둥(0)이 있으면 불가


#             # result에서 해당 프레임 삭제
#             for i in range(len(result)):
#                 result_x, result_y, result_a = result[i]
#                 if result_x == x and result_y == y and result_a == a:
#                     del result[i]
#                     break

#     # result를 x, y, a 순으로 정렬
#     result = sorted(result, key=lambda x:(x[0], x[1], x[2]))
            
#     # result 리턴
#     return result


n = 5
build_frame = 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))