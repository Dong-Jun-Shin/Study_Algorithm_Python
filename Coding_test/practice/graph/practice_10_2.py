# 팀 결성(서로소 집합)
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


def check_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    return a == b


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    else:
        print("YES") if check_parent(parent, a, b) else print("NO")

""" Test case
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
