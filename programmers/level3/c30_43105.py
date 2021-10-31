# 정수 삼각형
def solution(triangle):
    length = len(triangle)
    dp = []
    for tri_child in triangle:
        dp.append(tri_child[:])
    for i in range(1, length):
        for j in range(len(triangle[i]) - 1):
            for k in range(j, j + 2):
                # 현재 인덱스와 위 칸의 값 + 현재 칸의 값 중 큰 값 선택
                dp[i][k] = max(dp[i][k], dp[i - 1][j] + triangle[i][k])
    return max(dp[length - 1])


# lambda를 사용한 답안
# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])

# lambda 사용 답안을 풀어쓴 답안
# def solution(triangle, sum_list=[]):
#     if not triangle:
#         return max(sum_list)
#     else:
#         new_list = []
#         left_case = [0] + sum_list
#         right_case = sum_list + [0]
#         for x, y, z in zip(left_case, right_case, triangle[0]):
#             new_list.append(max(x, y) + z)
#         return solution(triangle[1:], new_list)

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
