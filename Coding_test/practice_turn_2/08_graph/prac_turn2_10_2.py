# 팀 결성
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


n, m = map(int, input().split())
graph = [i for i in range(n + 1)]

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(graph, a, b)
    elif oper == 1:
        if find_parent(graph, a) == find_parent(graph, b):
            print("YES")
        else:
            print("NO")