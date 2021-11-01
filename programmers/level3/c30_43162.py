# 네트워크
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union_parent(parent, i, j)
    # 매번 i, j가 같은지 확인하면서 find_parent로 업데이트하는거 대신
    # union 작업 후, 한번에 parent를 업데이트 시킴
    for i in range(n):
        find_parent(parent, i)
    return len(set(parent))


n = 5
computers = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]]
print(solution(n, computers))
