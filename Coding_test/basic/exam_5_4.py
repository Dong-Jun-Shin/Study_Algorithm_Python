from collections import deque

# 미로 크기 받기
n, m = map(int, input().split())

# 미로 정보 받기
mapInfo = []
for i in range(n):
    mapInfo.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 탐색 구현
def bfs(x, y) -> int:
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로를 벗어나는 경우
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            # 벽을 만난 경우
            if mapInfo[nx][ny] == 0:
                continue
            # 길을 만난 경우
            if mapInfo[nx][ny] == 1:
                mapInfo[nx][ny] = mapInfo[x][y] + 1
                queue.append((nx, ny))
    return mapInfo[n - 1][m - 1]


print(bfs(0, 0))
