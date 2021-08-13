# 감시 피하기
n = int(input())
graph = []
location_t = []
for i in range(n):
    datas = list(input().split())
    graph.append(datas)
    for j in range(len(datas)):
        if datas[j] == 'T':
            location_t.append((i, j))


def watch_check():
    for i in range(len(location_t)):
        # 행 확인
        t_x, t_y = location_t[i]
        for x in range(t_x - 1, -1, -1):
            if graph[x][t_y] == 'O':
                break
            elif graph[x][t_y] == 'S':
                return True
        for x in range(t_x + 1, n):
            if graph[x][t_y] == 'O':
                break
            elif graph[x][t_y] == 'S':
                return True
        # 열 확인
        for y in range(t_y - 1, -1, -1):
            if graph[t_x][y] == 'O':
                break
            elif graph[t_x][y] == 'S':
                return True
        for y in range(t_y + 1, n):
            if graph[t_x][y] == 'O':
                break
            elif graph[t_x][y] == 'S':
                return True
    else:
        return False


def dfs(wall):
    if wall < 3:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    if dfs(wall + 1):
                        return True
                    graph[i][j] = 'X'
    else:
        if not watch_check():
            return True
    return False


if dfs(0):
    print("YES")
else:
    print("NO")
