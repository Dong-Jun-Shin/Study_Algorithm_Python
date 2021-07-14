import time

# 가로 세로 받기
n, m = map(int, input().split())

# 2차원 리스트로 맵 정보 받기
trays = []
for i in range(n):
    trays.append(list(map(int, input())))

start_time = time.time()


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y) -> bool:
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if trays[x][y] == 0:
        trays[x][y] = 1
        dfs(x - 1, y)       # 상
        dfs(x + 1, y)       # 하
        dfs(x, y - 1)       # 좌
        dfs(x, y + 1)       # 우
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j):
            result += 1

print(result)

end_time = time.time()
print(f'소요된 시간: {end_time - start_time}')
