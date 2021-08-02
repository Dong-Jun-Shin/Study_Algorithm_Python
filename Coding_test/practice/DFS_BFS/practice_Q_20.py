# 감시 피하기
n = int(input())
graph = [[] for _ in range(n)]
location_t = []
for i in range(n):
    data = list(input().split())
    graph[i] = data
    for j in range(len(data)):
        if data[j] == 'T':
            location_t.append((i, j))


def check_horizon(x, y):
    for i in range(y - 1, -1, -1):
        if graph[x][i] == 'O':
            break
        elif graph[x][i] == 'S':
            return False
    for i in range(y + 1, n, 1):
        if graph[x][i] == 'O':
            break
        elif graph[x][i] == 'S':
            return False
    return True

def check_vertical(x, y):
    for i in range(x - 1, -1, -1):
        if graph[i][y] == 'O':
            break
        elif graph[i][y] == 'S':
            return False
    for i in range(x + 1, n, 1):
        if graph[i][y] == 'O':
            break
        elif graph[i][y] == 'S':
            return False
    return True

def dfs(wall_cnt):
    if wall_cnt == 3:
        # 벽 3개일 떄, 확인 과정
        for teacher in location_t:
            x, y = teacher
            catch_h_bool = check_horizon(x, y)
            catch_v_bool = check_vertical(x, y)
            if not (catch_h_bool and catch_v_bool):
                break
        else:
            return True
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    wall_cnt += 1
                    if dfs(wall_cnt) == True:
                        return True
                    graph[i][j] = 'X'
                    wall_cnt -= 1
    return False

if dfs(0):
    print("YES")
else:
    print("NO")
