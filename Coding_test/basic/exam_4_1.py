""" index 함수를 사용하는것이 for문보다 더 빠르다 """
"""------------------------------book
# 공간 크기와 계획 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0 , 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    # 교재 코드
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 내가 작성한 코드
    i = move_types.index(plan)
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
----------------------------------"""
# ---------------------------------me
# 공간 크기 받기
n = int(input())

# 이동 계획서 받기
moveList = list(map(str, input().split()))

row, col = 1, 1

for moveStr in moveList:
    if moveStr == "L" and col > 1:
        col -= 1
    elif moveStr == "R" and col < n:
        col += 1
    elif moveStr == "U" and row > 0:
        row -= 0
    elif moveStr == "D" and row < n:
        row += 1

print(f'{row} {col}')
# -----------------------------------
