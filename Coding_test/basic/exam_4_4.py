"""map은 여러개의 변수를 한번에 받기 가능, 리스트 컴프리헨션을 통해 2차원 리스트 초기화"""
"""------------------------------book
# 맵 크기 받기
n, m = map(int, input().split())
# [n][m] 리스트 생성 - 리스트 컴프리헨션
chkMap = [[0] * m for _ in range(n)]
step = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 캐릭터 좌표 받기
chaCodi = list(map(int, input().split()))

# 맵 정보 받기
mapList = []
for i in range(size[1]):
    mapList.append(list(map(int, input().split())))

# 처음 시작 위치의 육지
result = 1
# 시작점 체크
chkMap[chaCodi[0]][chaCodi[1]] = 1
while True:
    # 1. 갈 곳 정하기
    for i in range(1, 5):
        row = chaCodi[0]
        col = chaCodi[1]

        # 왼쪽으로 방향 전환
        direction = (4 + chaCodi[2] - i) % 4

        # 이동할 위치 설정
        row += step[direction][0]
        col += step[direction][1]

        # 가보지 않은 경우
        if chkMap[row][col] == 0 and mapList[row][col] == 0:
            # 회전 수 초기화
            i = 0
            # 방문 체크
            chkMap[row][col] = 1
            # 이동 횟수 증가
            result += 1
            # 이동
            chaCodi[0] = row
            chaCodi[1] = col
            chaCodi[2] = direction
            break
        # 회전한 이후, 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            continue

    # 4곳 다 가고 바다라서 뒤로 이동했는데 바다인 경우, 멈춤
    if i == 4:
        row = chaCodi[0] - step[direction][0]
        col = chaCodi[1] - step[direction][1]
        if mapList[row][col] == 0:
            chaCodi[0] = row
            chaCodi[1] = col
        else:
            break

print(result)
----------------------------------"""
# ---------------------------------me
import copy

# 맵 크기 받기
size = list(map(int, input().split()))
# [size[0]][size[1]] 리스트 생성
mapList = []
step = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 캐릭터 좌표 받기
chaCodi = list(map(int, input().split()))

# 맵 정보 받기
for i in range(size[0]):
    mapList.append(list(map(int, input().split())))
chkMap = copy.deepcopy(mapList)

# 처음 시작 위치의 육지
result = 1


chkMap[chaCodi[0]][chaCodi[1]] = 1     # 시작점 체크
while True:
    # 1. 갈 곳 정하기
    for i in range(1, 5):
        row = chaCodi[0]
        col = chaCodi[1]

        # 왼쪽으로 방향 전환
        direction = (4 + chaCodi[2] - i) % 4

        # 이동할 위치 설정
        row += step[direction][0]
        col += step[direction][1]

        # 가보지 않은 경우
        if chkMap[row][col] == 0 and mapList[row][col] == 0:
            # 회전 수 초기화
            i = 0
            # 방문 체크
            chkMap[row][col] = 1
            # 이동 횟수 증가
            result += 1
            # 이동
            chaCodi[0] = row
            chaCodi[1] = col
            chaCodi[2] = direction
            break
        # 회전한 이후, 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            continue

    # 4곳 다 가고 바다라서 뒤로 이동했는데 바다인 경우, 멈춤
    if i == 4:
        row = chaCodi[0] - step[direction][0]
        col = chaCodi[1] - step[direction][1]
        if mapList[row][col] == 0:
            chaCodi[0] = row
            chaCodi[1] = col
        else:
            break

print(result)
# -----------------------------------
