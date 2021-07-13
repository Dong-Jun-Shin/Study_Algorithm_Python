"""이동 경로를 미리 선언해서 for문을 통해 순차적으로 확인하는 방법이 있다. 속도는 비슷하다"""
"""------------------------------book
# 나이트 좌표 받기
codi = input()

result = 0
steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
xCodi = int(ord(codi[0]) - ord('a') + 1)    # a 문자의 97을 빼서 1로 변환
yCodi = int(codi[1])

for step in steps:
    next_xCodi = xCodi + step[0]
    next_yCodi = yCodi + step[1]

    if next_xCodi >= 1 and next_xCodi <= 8 and next_yCodi  >= 1 and next_yCodi <= 8:
        result += 1

print(result)
----------------------------------"""
# ---------------------------------me
# 나이트 좌표 받기
codi = input()

result = 0
firstMoveList = [-2, 2]                     # L자 이동 중 첫번째 이동
secondMoveList = [-1, 1]                    # L자 이동 중 두번째 이동
xCodi = int(ord(codi[0]) - ord('a') + 1)    # a 문자의 97을 빼서 1로 변환
yCodi = int(codi[1])

for x in firstMoveList:
    for y in secondMoveList:
        if xCodi + x >= 1 and xCodi + x <= 8 and yCodi + y >= 1 and yCodi + y <= 8:
            result += 1

        if yCodi + x >= 1 and yCodi + x <= 8 and xCodi + y >= 1 and xCodi + y <= 8:
            result += 1

print(result)
# -----------------------------------
