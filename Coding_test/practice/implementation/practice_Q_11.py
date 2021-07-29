# 뱀
from collections import deque

# 보드 크기 받기
n = int(input())
board = [[0] * n for _ in range(n)]

# 사과 개수와 위치 받기
appleCnt = int(input())
for i in range(appleCnt):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 9

# 방향 정보 받기
moveCnt = int(input())
moveList = [[] for _ in range(moveCnt)]
for i in range(moveCnt):
    moveList[i] = (input().split())

# 경과 시간
endTime = 0
# 뱀에 관한 변수
snake = deque()
snakeHead = [0, 0]
snakeTail = [0, 0]
board[0][0] = 1
# 방향에 대한 변수
wayList = [(-1, 0), (0, 1), (1, 0), (0, -1)]
way = 1
moveCnt = 0
# 게임 시작
while True:
    endTime += 1
    appleBool = False
    moveX, moveY = wayList[way]
    snakeHead[0] += moveX
    snakeHead[1] += moveY

    # 벽이거나 자기 몸이면 정지
    if (0 > snakeHead[0] or snakeHead[0] >= n) or (0 > snakeHead[1] or snakeHead[1] >= n):
        print(endTime)
        break
    if board[snakeHead[0]][snakeHead[1]] == 1:
        print(endTime)
        break
    
    # 이동과 사과에 대한 처리
    if board[snakeHead[0]][snakeHead[1]] == 9:
        appleBool = True

    board[snakeHead[0]][snakeHead[1]] = 1
    snake.append((snakeHead[0], snakeHead[1]))

    if not appleBool:
        board[snakeTail[0]][snakeTail[1]] = 0
        nextX, nextY = snake.popleft()
        snakeTail = [nextX, nextY]
    
    # 방향전환할 시간인지 확인
    if moveCnt < len(moveList) and endTime == int(moveList[moveCnt][0]):
        if moveList[moveCnt][1] == 'L':
            way = (way - 1) % 4
        elif moveList[moveCnt][1] == 'D':
            way = (way + 1) % 4
        moveCnt += 1
